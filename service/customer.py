from data import customer as data
from model.customer import Customer

def get_all() -> list[Customer]:
    return data.get_all()

def get_customer(customer_name) -> Customer | None:
    return data.get_customer(customer_name)