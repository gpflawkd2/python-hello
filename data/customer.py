from model.customer import Customer

_fake_datas = [
    Customer(name="jane", home="Seoul", call_num="010-1234-5678", email="jane@gmail.com"),
    Customer(name="rax", home="Sejong", call_num="010-1234-5678", email="rax@gmail.com")
    ]

def get_all() -> list[Customer]:    
    return _fake_datas

def get_customer(customer_name) -> Customer | None:
    for _fake_data in _fake_datas:
        if _fake_data.name == customer_name:
            return _fake_data
    return None