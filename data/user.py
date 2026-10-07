from model.user import User, DB_User
from .init import conn, curs, IntegrityError
from error import Missing, Duplicate

curs.execute("""
             CREATE TABLE IF NOT EXISTS user (
                 name TEXT PRIMARY KEY,
                 email TEXT,
                 hashed_password text
             )
             """)

def row_to_model(row : tuple) -> DB_User:
    name, email, hashed_password = row
    return DB_User(
        name=name, 
        email=email,
        hashed_password=hashed_password
        )
    
def model_to_dict(user: User | DB_User):
    return user.model_dump()

def find_user(username):
    sql = "SELECT * FROM user WHERE name = :name"
    params = {"name": username}
    curs.execute(sql, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    return row

def create_user(user:DB_User):
    sql = """
        insert into user (name, email, hashed_password)
        values (:name, :email, :hashed_password)
    """
    params = model_to_dict(user)
    try:
        curs.execute(sql, params)
    except IntegrityError:
        raise Duplicate(msg="already exists")
    conn.commit()
    return None