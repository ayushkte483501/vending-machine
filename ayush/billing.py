
# billing.py

# it work as 
# price,quantity -> calculation -> subtotal

import numpy as npy  # funtion


def calculate_subtotal(price, quantity):

    prices = npy.array([price])
    quantities = npy.array([quantity])

    subtotal = npy.sum(prices * quantities)

    return subtotal

    # after this discount.py