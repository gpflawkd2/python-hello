from fastapi import APIRouter, Request
from model.customer import Customer
from service import customer as service
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter(prefix="/html")

templates = Jinja2Templates(directory="templates")

@router.get("", response_class=HTMLResponse)
def get_all(request:Request):
    customers = service.get_all()
    return templates.TemplateResponse(request, "home.html",
                                      {"customers": customers})

