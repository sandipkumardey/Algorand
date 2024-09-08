# Question: Write a Python program to find the average of n numbers using a list.

def average_of_list(lst):
    return sum(lst) / len(lst) if lst else 0

# Example usage:
n = int(input("Enter the number of elements: "))
lst = [int(input(f"Enter number {i+1}: ")) for i in range(n)]
average = average_of_list(lst)
print(f"The average of the list is: {average}")
