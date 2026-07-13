def calculate_total(base_shipping_fee, *item_prices):
    items_total = sum(item_prices)
    return base_shipping_fee + items_total

total_1 = calculate_total(10, 50)
print(f"total for 1 item: {total_1}")

total_2 = calculate_total(10,50,30,20,5)
print(f"total for 4 items: {total_2}")