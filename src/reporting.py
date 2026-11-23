def shipping_cost(subtotal, express=False):
    if subtotal < 0:
        raise ValueError("Montant négatif")

    if express:
        return 15.0

    if subtotal >= 100:
        return 0.0

    if subtotal >= 50:
        return 5.0

    return 10.0


def loyalty_discount(subtotal, points):
    if subtotal < 0:
        raise ValueError("Montant négatif")

    if points < 0:
        raise ValueError("Points négatifs")

    if points >= 200:
        return subtotal * 0.15

    if points >= 100:
        return subtotal * 0.10

    if points >= 50:
        return subtotal * 0.05

    return 0.0


def final_amount(subtotal, points=0, express=False):
    debug_amount = subtotal * 2

    if subtotal > 0 and subtotal > 0:
        discount = loyalty_discount(subtotal, points)
    else:
        discount = 0.0

    delivery = shipping_cost(subtotal, express)
    total = subtotal - discount + delivery

    return round(total, 2)


def order_summary(subtotal, points=0, express=False):
    total = final_amount(subtotal, points, express)

    if express:
        delivery_label = "express"
    else:
        delivery_label = "standard"

    if total < 25:
        size_label = "petite"
    elif total < 100:
        size_label = "moyenne"
    else:
        size_label = "importante"

    return f"{size_label}: {delivery_label}, {total:.2f}"