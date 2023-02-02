"""
Lab 3
Author: Heriberto Lopez
Class: COP3502C
Section: 29020
Description: Scientific Calculator
"""


import math

print("Current Result: 0.0\n")
print('''Calculator Menu 
--------------- 
0. Exit Program
1. Addition 
2. Subtraction 
3. Multiplication 
4. Division
5. Exponentiation
6. Logarithm
7. Display Average
''')

operation: int = int(input("Enter Menu Selection: "))
if operation == 7:
    print("No calculations yet to average!")
    operation: int = int(input("Enter Menu Selection: "))
if operation == 0:
    print("Thanks for using this calculator. Goodbye!")
elif operation == 1:
    first_operand = float(input("Enter first operand: "))
    second_operand = float(input("Enter second operand: "))
    result = first_operand + second_operand
    print(f"Current Result: {result}")
elif operation == 2:
    first_operand = float(input("Enter first operand: "))
    second_operand = float(input("Enter second operand: "))
    result = first_operand - second_operand
    print(f"Current Result: {result}")
elif operation == 3:
    first_operand = float(input("Enter first operand: "))
    second_operand = float(input("Enter second operand: "))
    result = first_operand * second_operand
    print(f"Current Result: {result}")
elif operation == 4:
    first_operand = float(input("Enter first operand: "))
    second_operand = float(input("Enter second operand: "))
    result = first_operand / second_operand
    print(f"Current Result: {result}")
elif operation == 5:
    first_operand = float(input("Enter first operand: "))
    second_operand = float(input("Enter second operand: "))
    result = first_operand ** second_operand
    print(f"Current Result: {result}")
elif operation == 6:
    first_operand = float(input("Enter first operand: "))
    second_operand = float(input("Enter second operand (base): "))
    result = math.log(first_operand, second_operand)
    print(f"Current Result: {result}")
elif operation == 7:

else:
    print("Error: Invalid selection! Terminating program.")
