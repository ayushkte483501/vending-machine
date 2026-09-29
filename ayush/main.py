
# main.py

from menu import (
    show_menu,
    show_drinks,
    show_chocolate,
    show_chips,
    show_juice
)

from product import (
    drinks,
    chocolate,
    chips,
    juice
)

from billing import calculate_subtotal

from discount import apply_discount

from payment import process_payment

from receipt import print_receipt

from validation import (
    get_section,
    get_order,
    get_quantity
)


# PRODUCT SELECTION

def select_product(section):

    if section == 1:

        show_drinks()

        order = get_order()

        if order is None:
            return None, None

        return drinks[order]


    elif section == 2:

        show_chocolate()

        order = get_order()

        if order is None:
            return None, None

        return chocolate[order]


    elif section == 3:

        show_chips()

        order = get_order()

        if order is None:
            return None, None

        return chips[order]


    elif section == 4:

        show_juice()

        order = get_order()

        if order is None:
            return None, None

        return juice[order]



# MAIN PROGRAM

while True:

    show_menu()

    # Section

    section = get_section()

    if section is None:
        continue


    # Exit

    if section == 5:

        print("Thank you!")

        break


    # Product

    item, price = select_product(section)

    if item is None:

        print("\nWant something else!")

        continue


    # Quantity

    quantity = get_quantity()

    if quantity is None:
        continue


    # Subtotal

    subtotal = calculate_subtotal(price,quantity)

    print("\nSubtotal: Rs.", subtotal)


    # Discount

    discount_percent, discount, final_amount = apply_discount(subtotal)

    print("Lucky Discount:", discount_percent, "%")

    print("Discount: Rs.", discount)

    print("Amount to pay: Rs.", final_amount)


    # Payment

    money, change = process_payment(final_amount)

    if money is None:
        continue


    # Successful purchase

    print("\nYour selected item is:", item)

    print("Your change is: Rs.", change)

    print("Please collect your item")


    # Receipt

    print_receipt(
        item,
        price,
        quantity,
        subtotal,
        discount_percent,
        discount,
        final_amount,
        money,
        change
    )


    # Buy again

    again = input("\nDo you want to buy something else? -> (Yes/No): ")

    if again.lower() == "no":

        print("\nThank you for using the vending machine")

        print("------------ Have a nice day! ------------")

        break

# after this product.py