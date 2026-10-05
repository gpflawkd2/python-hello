from fastapi import APIRouter
from model.customer import Customer
import service.customer as service

router = APIRouter(prefix="/customer")

@router.get("/")
def get_all() -> list[Customer]:
    return service.get_all()

@router.get("/{customer_name}")
def get_customer(customer_name) -> Customer | None:
    return service.get_customer(customer_name)