from model.market import Market

_fake_datas = [
    Market(name="피자나라", location="Seoul", menu={"pizza": 10000, "burger": 8000}, call_num="02-1234-5678"),
    Market(name="레스토랑", location="Sejong", menu={"pasta": 12000, "salad": 6000}, call_num="063-1234-5678")
    ]

def get_all() -> list[Market]:    
    return _fake_datas

def get_market(market_name) -> Market | None:
    for _fake_data in _fake_datas:
        if _fake_data.name == market_name:
            return _fake_data
    return None