
# test_vending.py

# it work as
# subtotal -> discount

from billing import calculate_subtotal
from discount import apply_discount


# Test 1: Subtotal

subtotal = calculate_subtotal(50, 2)

print("Test 1 - Subtotal:", subtotal)

if subtotal == 100:
    print("PASS")   
else:
    print("FAIL")


# Test 2: Discount

discount_percent, discount, final_amount = apply_discount(100)

print("\nTest 2 - Discount")
print("Discount:", discount)
print("Final Amount:", final_amount)

if final_amount <= 100:
    print("PASS")
else:
    print("FAIL")

# after this readme.md