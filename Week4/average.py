# keeps reading numbers until the user enters a 0
# program should print out eachof the numbers entered and the average of them

numbers = []

#first number then we check if it is 0 in the whie loop

number = int(input("Enter number (0 to quit): "))

while number != 0:
    numbers.append(number)

    #read the next number and check if 0
    number = int(input("enter another (0 to quit):"))
            
for value in numbers:
    print(value)

# I want average to be a float
average = float(sum(numbers)) / len(numbers)
print (f"The average is {average}")
