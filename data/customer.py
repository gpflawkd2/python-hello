from model.customer import Customer
import sqlite3
from .init import conn, curs

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

"""
def get_all() -> list[Customer]:    
    return _fake_datas

def get_customer(customer_name) -> Customer | None:
    for _fake_data in _fake_datas:
        if _fake_data.name == customer_name:
            return _fake_data
    return None
"""