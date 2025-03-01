# reads in a student percentage mark and prints out correspondeing the grade 
# program should check that the percentage is valid

percentage = float(input("Enter the percentage: "))
print (percentage)

#be careful with ands and or
if percentage < 0 or percentage > 100:
    # later will show you error handling
    # this should really throw an error

    print ("Please enter a number between 0 and 100")
elif percentage < 40:# we know it is greater than 0
    print ("Fall")
elif percentage < 50: # between 40 and 49
    print ("Pass")
elif percentage < 60: # between 50 and 59
    print ("Merit1")
elif percentage < 70: # between 60 and 69
    print ("Merit2")
else: # the only option left is between 70 and 100
    print ("Distinction")