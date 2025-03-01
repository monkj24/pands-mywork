# Give the absolute value of a number

# Author Joanna Mnich

# In the question, number is ambiguous( integer or float, minus and plus) but the
# output  tell us that the we should be dealing with floats
# So I am casting the input to a float

number = float(input("Enter a number:"))
absoluteValue = abs(number)
print('The absolute value of {} is {}'.format(number, absoluteValue))