# Demonstrate raising a exception
# This program prompts to user for an amount and withdraws it from an account


balance = 100

def withdraw(amount):
    global balance
    if amount < 0: 
        raise ValueError(" amount should always be greater then 0")
    balance =balance - amount
    return balance

amount = int(input("amount to withdraw:"))
print (withdraw(amount))
