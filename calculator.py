# Question: Write a program in Python to implement a simple calculator.

def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Division by zero is not allowed."
    else:
        return "Invalid operation."

# Example usage:
operation = input("Enter operation (add, subtract, multiply, divide): ").lower()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = calculator(operation, num1, num2)
print(f"Result: {result}")
