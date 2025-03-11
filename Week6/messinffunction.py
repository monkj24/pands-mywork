# messing more with functions
#flexible arguments

print(1,2,3, sep="", end="\t")
print("hi")

def fun1(*args):
    print(type(args))
    for val in args:
        print(val)
    
def fun2(** kwargs):
    print(type(kwargs))
    print(kwargs)
    #for val in args:
    #print(val)

fun2(name="joe", age=21, gender ="m")

#sample code
def ave(*values):
    number_of_values = len(values)
    sum= 0
    for value in values:
        sum+=value 
    
    average = sum / number_of_values
    return average , sum

print(ave(1,2,3,4,5,6))

av1, sum_of_numbers = ave(1,2,3,4,5,6)

print(f"{avi} and sum is {sum_of_numbers}")

