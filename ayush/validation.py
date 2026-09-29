
# validation.py

# it work as
# user input -> validation -> valid -> continue
#                                   |-> invalid -> error message


def get_section():

    try:

        section = int(
            input("\nChoose section of your choice: ")
        )

        if section < 1 or section > 5:

            print("Please choose a section from 1 to 5")

            return None

        return section

    except ValueError:

        print("Please enter a valid number")

        return None


def get_order():

    try:

        order = int(input("\nSelect your item: "))

        if order < 1 or order > 4:

            print("Please select an item from 1 to 4")

            return None

        return order

    except ValueError:

        print("Please enter a valid number")


def get_quantity():

    try:

        quantity = int(
            input("\nEnter quantity of item: ")
        )

        if quantity <= 0:

            print("Quantity must be greater than zero")

            return None

        return quantity

    except ValueError:

        print("Please enter a valid quantity")

        return None

# after this test_vending.py