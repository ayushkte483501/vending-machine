# Problem Statement

## Vending Machine System

Design and develop a Python-based vending machine system that allows users to select products from different categories, enter the required quantity, make a payment, and receive the correct change.

The vending machine should provide products from the following categories:

- Drinks
- Chocolate
- Chips
- Juice

The system should display the available products along with their prices and allow the user to select a product and quantity.

After selection, the program should calculate the subtotal using NumPy. A random discount should then be generated and applied to calculate the final amount payable.

The system should accept the customer's payment and check whether the entered amount is sufficient. If the payment is sufficient, the machine should calculate and display the change. If the payment is insufficient, the system should inform the user about the additional amount required.

The program should generate a detailed receipt containing:

- Selected item
- Item price
- Quantity
- Subtotal
- Discount percentage
- Discount amount
- Final bill
- Amount paid
- Change received

The system should also handle invalid inputs such as non-numeric values, invalid menu selections, invalid quantities, and insufficient payment without crashing.

The project should follow a modular programming approach. Different tasks such as product management, menu display, billing, discount calculation, payment processing, receipt generation, and input validation should be implemented in separate Python modules.

## Main Requirements

1. Display the vending machine menu.
2. Display products and their prices.
3. Allow the user to select a product category.
4. Allow the user to select an item.
5. Allow the user to enter the quantity.
6. Calculate the subtotal using NumPy.
7. Generate and apply a random discount.
8. Calculate the final amount.
9. Accept and validate customer payment.
10. Calculate the change.
11. Generate a detailed receipt.
12. Handle invalid inputs safely.
13. Allow the user to make another purchase.
14. Provide a separate testing module for important calculations.

## Technologies Used

- Python
- NumPy
- Math module
- Random module
- Modular Python programming

## Expected Outcome

The final system should provide a simple and user-friendly vending machine experience while demonstrating the use of Python functions, modules, loops, conditional statements, exception handling, NumPy, random values, mathematical calculations, and basic software testing.s