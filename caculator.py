def calculate_discount(price: float, discount_percent: float) -> float:
    # Lỗi cố ý: trừ trực tiếp số phần trăm thay vì chia 100
    return price - discount_percent
