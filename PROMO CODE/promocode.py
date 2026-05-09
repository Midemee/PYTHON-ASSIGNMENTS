def apply_discount(item_name, price, promo_code):
    
    if promo_code.upper() == "SAVE10":
        discount = price * 0.10
        final_price = price - discount
    elif promo_code.upper() == "HALFOFF":
        discount = price * 0.50
        final_price = price - discount
    else:
        price = price
        final_price = price
    return round(final_price, 2)
        

