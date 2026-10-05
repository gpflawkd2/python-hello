from model.customer import Customer, CustomerUpdate
import sqlite3
from .init import conn, curs
from error import Missing, Duplicate

curs.execute("""
             CREATE TABLE IF NOT EXISTS customers (
                 name TEXT PRIMARY KEY,
                 home TEXT,
                 call_num TEXT,
                 email TEXT
             )
             """)

def row_to_model(row : tuple) -> Customer:
    name, home, call_num, email = row
    return Customer(
        name=name, 
        home=home, 
        call_num=call_num, 
        email=email
        )
    
def model_to_dict(customer: Customer) -> dict:
    return customer.model_dump()

# 모든 고객 조회
def get_all() -> list[Customer]:    
    sql = "SELECT * FROM customers"
    curs.execute(sql)
    datas = curs.fetchall()
    return [row_to_model(data) for data in datas]
   
# 새로운 고객 생성
def create_customer(new_customer: Customer) -> Customer:
    sql = "INSERT INTO customers (name, home, call_num, email) VALUES (:name, :home, :call_num, :email)"
    params = model_to_dict(new_customer)
    try:
        curs.execute(sql, params)
    except sqlite3.IntegrityError:
        raise Duplicate(msg=f"customer {new_customer.name} is already exists")
    
    conn.commit()
    return get_customer(new_customer.name)

# 특정 고객 조회
def get_customer(customer_name) -> Customer | None:
    sql = "SELECT * FROM customers WHERE name = :name"
    params = {"name": customer_name}
    curs.execute(sql, params)
    data = curs.fetchone()
    if data:
        return row_to_model(data)
    raise Missing(f"customer {customer_name} not found")

# 기존 고객 업데이트
def modify_customer(customer_name: str, modified_customer: CustomerUpdate) -> Customer:
    sql = """
        UPDATE customers
        SET home = :home, call_num = :call_num, email = :email
        WHERE name = :customer_name
    """
    params = model_to_dict(modified_customer)
    params["customer_name"] = customer_name
    curs.execute(sql, params)
    if curs.rowcount == 1:
        conn.commit()
        return get_customer(customer_name)
    else :
        raise Missing(msg=f"customer {customer_name} not found")
    
# 고객 삭제
def delete_customer(customer_name: str) -> None:
    sql = "DELETE FROM customers WHERE name = :name"
    params = {"name": customer_name}
    curs.execute(sql, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"customer {customer_name} not found")
    conn.commit()
    return None
