from data import customer as data
from model.customer import Customer, CustomerUpdate

def get_all() -> list[Customer]:
    return data.get_all()

def get_customer(customer_name) -> Customer | None:
    return data.get_customer(customer_name)

def create_customer(new_customer: Customer) -> Customer:
    return data.create_customer(new_customer)

def modify_customer(customer_name: str, modified_customer: CustomerUpdate) -> Customer:
    return data.modify_customer(customer_name, modified_customer)

def delete_customer(customer_name: str) -> None:
    return data.delete_customer(customer_name)  