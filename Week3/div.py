# program that reads in two numbers and
#outputs the integer answer and remainder

x = int(input ("Enter first number: "))
y = int(input ("Enter the nnumber you want to divide by: "))
answer = int(x//y) # // gives the int division
reminder = x%y  # % gives the reminder

print("{} divided by {} is {} with reminder {}".format( x, y, answer, reminder))