# Question: Write a program that computes the net amount of a bank account based on a transaction log from console input.

def compute_net_amount():
    net_amount = 0
    print("Enter the transaction log (type '!' to finish):")
    while True:
        transaction = input()
        if transaction == "!":
            break
        action, amount = transaction.split()
        amount = int(amount)
        if action == "D":
            net_amount += amount
        elif action == "W":
            net_amount -= amount
    return net_amount

# Example usage:
net_amount = compute_net_amount()
print(f"The net amount in the bank account is: {net_amount}")
