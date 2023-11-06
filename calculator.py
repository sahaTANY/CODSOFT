#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def main():
    operation_map = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide
    }

    print("Welcome to the Simple Calculator!")

    while True:
        print("Available operations: +, -, *, /")

        x = float(input("Enter first number: "))
        operation = input("Enter operation: ")
        y = float(input("Enter second number: "))

        if operation not in operation_map:
            print("Invalid operation. Please enter correct operation.")
            continue

        result = operation_map[operation](x, y)
        print(f"Result: {result}")

        # Ask the user if they want to continue
        while True:
            print("Do you want to continue calculating? (yes/no)")
            answer = input().lower()
            if answer == 'yes':
                break
            elif answer == 'no':
                print("Exiting the calculator.")
                return
            else:
                print("Invalid answer. Please enter 'yes' or 'no'.")

if __name__ == '__main__':
    main()


# In[ ]:




