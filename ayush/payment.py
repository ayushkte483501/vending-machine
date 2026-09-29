
# payment.py

# it work as
# final amount -> customer enters money -> enough? -> no -> error
#                                                  |-> yes -> change


def process_payment(final_amount):

    try:

        money = int(input("\nEnter the money: Rs."))

        if money >= final_amount:

            change = money - final_amount

            return money, change

        else:

            print("\nNot enough money!")
            print("You need Rs.", final_amount - money, "more")

            return None, None

    except ValueError:

        print("Please enter a valid amount")

        return None, None