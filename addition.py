# Question: Write a program in Python to find the addition & average of three float numbers.

def addition_and_average(num1, num2, num3):
    # Calculate the sum of the numbers
    total_sum = num1 + num2 + num3
    # Calculate the average
    average = total_sum / 3
    return total_sum, average

# Example usage:
num1, num2, num3 = 4.5, 7.8, 2.1
total_sum, average = addition_and_average(num1, num2, num3)
print(f"Sum: {total_sum}, Average: {average}")
