from fastapi import APIRouter, HTTPException
from model.customer import Customer, CustomerUpdate
import service.customer as service

router = APIRouter(prefix="/customer")

@router.get("/")
def get_all() -> list[Customer]:
    return service.get_all()

@router.get("/{customer_name}")
def get_customer(customer_name) -> Customer | None:
    return service.get_customer(customer_name)

@router.put("/{customer_name}")
def modify_customer(customer_name: str, modified_customer: CustomerUpdate) -> Customer:
    return service.modify_customer(customer_name, modified_customer)

@router.post("/")
def create_customer(new_customer: Customer) -> Customer:
    try:
        return service.create_customer(new_customer)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    
@router.delete("/{customer_name}")
def delete_customer(customer_name: str) -> None:
    return service.delete_customer(customer_name)