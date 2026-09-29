
# receipt.py

# it work as
# purchase information -> recepit

# taking all funtion into one

def print_receipt(item, price, quantity,
                  subtotal, discount_percent,
                  discount, final_amount,
                  money, change):

    print("\n")
# for looks
    print("=" * 20)
    print("              RECEIPT")
    print("=" * 20)
# designing receipt
    print("Item         :", item)
    print("Price        : Rs.", price)
    print("Quantity     :", quantity)
    print("Subtotal     : Rs.", subtotal)
    print("Discount     :", discount_percent, "%")
    print("Discount Rs. :", discount)
    print("Final Bill   : Rs.", final_amount)
    print("Paid         : Rs.", money)
    print("Change       : Rs.", change)
# for bottom greeting
    print("=" * 20)
    print("      Thank you for shopping !")
    print("=" * 20)
    
# after this validation.py