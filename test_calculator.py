from calculator import calculate_discount

def test_calculate_discount():
    # 100 giảm 20% phải ra 80
    assert calculate_discount(100.0, 20.0) == 80.0
