
# discount.py

# it work as 
# subtotal -> random -> maths rounding -> final amount

import random
import math


def apply_discount(subtotal):

    discount_percent = random.choice([0, 5, 10, 15, 20])

    discount = subtotal * (discount_percent / 100)

    discount = math.floor(discount + 0.5)

    final_amount = subtotal - discount

    return discount_percent, discount, final_amount

    # after this payment.py