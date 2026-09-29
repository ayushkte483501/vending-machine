# Vending Machine Project

## 1. Project Overview

This project is a Python-based Vending Machine system.

The program allows a customer to select a category, choose a product, enter the quantity, calculate the bill, receive a random discount, make a payment, receive change, and generate a receipt.

The project is divided into multiple Python modules. Each module performs a specific task, which makes the program easier to understand, maintain, test, and improve.

## 2. Objectives

The main objectives of this project are:

- To create a simple and user-friendly vending machine.
- To use Python programming concepts in a practical project.
- To divide the program into different modules.
- To use NumPy for numerical calculations.
- To use the random module for generating discounts.
- To use the math module for calculations.
- To implement input validation and error handling.
- To generate a detailed purchase receipt.
- To test important parts of the program.

## 3. Features

The vending machine provides the following features:

- Displays different product categories.
- Allows the user to select a product.
- Allows the user to enter the quantity.
- Calculates the subtotal.
- Provides a random discount.
- Calculates the final amount.
- Accepts customer payment.
- Calculates the change.
- Generates a receipt.
- Handles invalid user input.
- Allows the customer to purchase another item.
- Provides a separate testing file.

## 4. Product Categories

### Drinks

| No. | Item | Price |
|---|---|---:|
| 1 | Monster | Rs.100 |
| 2 | Zero Coke | Rs.40 |
| 3 | Pepsi | Rs.40 |
| 4 | Limca | Rs.30 |

### Chocolate

| No. | Item | Price |
|---|---|---:|
| 1 | Dairy Milk | Rs.50 |
| 2 | Milky Bar | Rs.30 |
| 3 | Snackers | Rs.40 |
| 4 | Munch | Rs.20 |

### Chips

| No. | Item | Price |
|---|---|---:|
| 1 | Spicy Lays | Rs.20 |
| 2 | Plain Lays | Rs.20 |
| 3 | Uncle Chips | Rs.30 |
| 4 | Doritos | Rs.50 |

### Juice

| No. | Item | Price |
|---|---|---:|
| 1 | Mango Juice | Rs.40 |
| 2 | Strawberry Juice | Rs.50 |
| 3 | Litchi Juice | Rs.40 |
| 4 | Apple Juice | Rs.45 |

## 5. Technologies Used

- Python
- NumPy
- Math module
- Random module
- VS Code

## 6. Project Structure

Vending Machine Project
│
├── main.py
├── products.py
├── menu.py
├── billing.py
├── discount.py
├── payment.py
├── receipt.py
├── validation.py
├── test_vending.py
└── README.md