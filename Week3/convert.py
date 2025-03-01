# bank takes amount in cent but
# may o may not be a minus sign (-9.44)
# takes in float amount of dollars and returns that absolute amoount in cent

# abs- bierze wartosc bezwzgledna by usunac minus 



number = float(input("Please enter amount:"))

converted = abs(int(number * 100))

print(input("The amount in cent is:"))
print(converted)


