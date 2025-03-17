# More messing with functins
#Anonymu###ous function

x =lambda argi: argi **2

answer = x(4)
print (answer)

businesstype = "standard"
businesstype = "reduced"

vatcalc = lambda amount: amount * 0.23

if businesstype =="reduced":
    vatcalc = lambda amount: amount * 0.135

cash = 10

print (vatcalc(cash))

# sort a list
numbers =[2,33,55,1,4]
sortednumbers = sorted(numbers)
print(f"{numbers} sorted is {sortednumbers}")

# sort dictionary
data = [{'first': 'Guido', 'last': 'Van','Yob': 1956},
        {'first': 'Grace', 'last': ' Hopper', 'Yob': 1986}]

sorteddate = sorted(data, key=lambda x: x['Yob'])
for item in sorteddate:
    print(item)

                   