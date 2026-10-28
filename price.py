def calculate_price(price: float, discount_percent: int) -> float:
    return price * (1 - discount_percent / 100)


result = calculate_price(1000.0, 20)
print(result)
