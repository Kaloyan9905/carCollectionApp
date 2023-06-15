def get_total_cars_price(cars):
    if cars:
        return sum([c.price for c in cars])
    return 0
