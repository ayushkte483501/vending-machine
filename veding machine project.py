# all important import funtions

import math # 1 for calculations
import random # 2 for discount
import numpy as npy # 3 for algebra

while True:

  # for looks

    print("=="*20)
    print("         VENDING MACHINE")
    print("=="*20)

  # showing different food, snaks and drinks

    print("1. Drinks")
    print("2. Chocolate")
    print("3. Chips")
    print("4. Juice")
    print("5. Exit")

  # for error handling cases

    try:
        section = int(input("\nChoose section of your choice: "))
    except ValueError:
        print("Can't decide !")
        continue

    # DRINKS
    # show every product avaliable in section 1

    if section == 1:
        print("\nDrinks")
        print("1. Monster - Rs.100")
        print("2. Zero Coke - Rs.40")
        print("3. Pepsi - Rs.40")
        print("4. Limca - Rs.30")

    # selection of choice

        Order = int(input("\nSlect your item: "))

    # define index, item and price

        if Order == 1:
            item = "Monster"
            price = 100
        elif Order == 2:
            item = "Zero Coke"
            price = 40
        elif Order == 3:
            item = "Pepsi"
            price = 40
        elif Order == 4:
            item = "Limca"
            price = 30
        else:
            print("\nWant something else !")
            continue

    # CHOCOLATE
    # show every product avaliable in section 2


    elif section == 2:
        print("\nChocolate")
        print("1. Dairy Milk - Rs.50")
        print("2. Milky Bar - Rs.30")
        print("3. Snackers - Rs.40")
        print("4. Munch - Rs.20")

    # selection of choice

        Order = int(input("\nSelect your item: "))

    # define index, item and price

        if Order == 1:
            item = "Dairy Milk"
            price = 50
        elif Order == 2:
            item = "Milky Bar"
            price = 30
        elif Order == 3:
            item = "Snackers"
            price = 40
        elif Order == 4:
            item = "Munch"
            price = 20
        else:
            print("\nWant something else !")
            continue

    # CHIPS
    # show every product avaliable in section 3

    elif section == 3:
        print("\nChips")
        print("1. Spicy Lays - Rs.20")
        print("2. Plain Lays - Rs.20")
        print("3. Uncle Chips - Rs.30")
        print("4. Doritos - Rs.50")

    # selection of choice

        Order = int(input("\nSelect your item: "))

    # define index, item and price

        if Order == 1:
            item = "Spicy Lays"
            price = 20
        elif Order == 2:
            item = "Plain Lays"
            price = 20
        elif Order == 3:
            item = "Uncle Chips"
            price = 30
        elif Order == 4:
            item = "Doritos"
            price = 50
        else:
            print("\nWant something else !")
            continue

    # JUICE
    # shkw every product avaliable in section 4

    elif section == 4:
        print("\nJuice")
        print("1. Mango - Rs.40")
        print("2. Strawberry - Rs.50")
        print("3. Litchi - Rs.40")
        print("4. Apple - Rs.45")

    # section of choice

        Order = int(input("\nSelect your item: "))

    # define index, item and price

        if Order == 1:
            item = "Mango Juice"
            price = 40
        elif Order == 2:
            item = "Strawberry Juice"
            price = 50
        elif Order == 3:
            item = "Litchi Juice"
            price = 40
        elif Order == 4:
            item = "Apple Juice"
            price = 45
        else:
            print("\nWant something else !")
            continue

    # incase for directly exiting the vending machine

    elif section == 5:
        print("Thank you!")
        break
    else:
        print("\nCan't decide !")
        continue

    # quantity
    # in case of error

    try:
        quantity = int(input("\nEnter quantity of item: "))
        if quantity <= 0:
            print("Quantity must be greater than zero")
            continue
    except ValueError:
        print("Please enter a valid quantity")
        continue

    # module 1: numpy

    prices = npy.array([price])   # based on algebra

    quantities = npy.array([quantity])

    subtotal = npy.sum(prices * quantities)

    print("\nSubtotal: Rs.", subtotal)

    # module 2: random discount

    discount_percent = random.choice([0, 5, 10, 15, 20])

    discount = (subtotal) * (discount_percent/100) # based on random funtion

    # module 3: maths
    # random discount -> final amount

    discount = math.floor(discount + 0.5) #based on calculation

    final_amount = subtotal - discount

    # now print for coustmer's details
    print("Lucky Discount:", discount_percent, "%")
    print("Discount: Rs.", discount)
    print("Amount to pay: Rs.", final_amount)

    # payment

    money = int(input("\nEnter the money: Rs."))

    if money >= final_amount:
        change = money - final_amount
        print("\nYour selected item is:", item)
        print("Your change is: Rs.", change)
        print("Please collect your item")

        # recipt
        # making of recipt slip

     # for top looks in recipt

        print("\n")

        print("="*40)
        print("              RECEIPT")
        print("="*40)

    # creating rows with specification

        print("Item         :", item)       # taken refence from actual bill

        print("Price        : Rs.", price)  # include all necessary deatils

        print("Quantity     :", quantity)

        print("Subtotal     : Rs.", subtotal)

        print("Discount     :", discount_percent, "%")

        print("Discount Rs. :", discount)

        print("Final Bill   : Rs.", final_amount)

        print("Paid         : Rs.", money)

        print("Change.      : Rs.", change)

     # for bottom details

        print("="*40)
        print("      Thank you for shopping !    ")
        print("="*40)
    else:
        print("\nNot enough money !")
        print("You need Rs.", final_amount - money, "more")

     # asking again for his final decision

    again = input("\nDo you want to buy something else? -> (Yes/No): ")

    if again.lower() == "no":
      # for ending the conversation with user
        print("\n Thank you for using the vending machine ")
        print("------------ Have a nice day! ------------")
        break