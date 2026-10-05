from fastapi import APIRouter, HTTPException
from model.customer import Customer, CustomerUpdate
import service.customer as service
from error import Missing, Duplicate

router = APIRouter(prefix="/customer")

@router.get("")
@router.get("/")
def get_all() -> list[Customer]:
    return service.get_all()

@router.get("/{customer_name}")
def get_customer(customer_name) -> Customer | None:
    try:
        return service.get_customer(customer_name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.put("/{customer_name}")
def modify_customer(customer_name: str, modified_customer: CustomerUpdate) -> Customer:
    try:
        return service.modify_customer(customer_name, modified_customer)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.post("/")
def create_customer(new_customer: Customer) -> Customer:
    try:
        return service.create_customer(new_customer)
    except Duplicate as e:
        raise HTTPException(status_code=404, detail=e.msg)

@router.delete("/{customer_name}")
def delete_customer(customer_name: str) -> None:
    try:
        return service.delete_customer(customer_name)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.msg)