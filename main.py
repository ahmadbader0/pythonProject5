# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import math


# Function to calculate the sum of two numbers
def add(x, y):
    return x + y


# Function to calculate the difference between two numbers
def subtract(x, y):
    return x - y


# Function to calculate the product of two numbers
def multiply(x, y):
    return x * y


# Function to calculate the division of two numbers
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y


# Function to calculate the area of a triangle
def calculate_triangle_area(base, height):
    return 0.5 * base * height


# Function to calculate the area of a circle
def calculate_circle_area(radius):
    return math.pi * (radius ** 2)


# Function to calculate the area of a rectangle
def calculate_rectangle_area(length, width):
    return length * width


# Main menu function
def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Calculate Triangle Area")
        print("6. Calculate Circle Area")
        print("7. Calculate Rectangle Area")
        print("8. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

        if choice == '8':
            print("Exiting the program. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
        elif choice == '5':
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("Triangle Area: ", calculate_triangle_area(base, height))
        elif choice == '6':
            radius = float(input("Enter the radius of the circle: "))
            print("Circle Area: ", calculate_circle_area(radius))
        elif choice == '7':
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("Rectangle Area: ", calculate_rectangle_area(length, width))
        else:
            print("Invalid input. Please choose a valid option (1/2/3/4/5/6/7/8).")


if __name__ == "__main__":
    main_menu()
