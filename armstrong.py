# Question: Write a Python program to check a number is Armstrong or not.

def is_armstrong(number):
    digits = [int(digit) for digit in str(number)]
    return sum(digit**len(digits) for digit in digits) == number

# Example usage:
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
