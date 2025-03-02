# Messing with dictionaries

# Author Joanna mnnich

car = {
    'make': 'ford',
    'model': 'mondeo',
    'year': 2006,
    'owner':'Andrew'
}

print (car)
print (car ['make'])

attr = 'year'
print (car[attr])

# dictonaries object
car = {
    'make': 'ford',
    'model': 'mondeo',
    'year': 2006,
    'owner': {
        'name': 'Andrew',
        'driver-number': 1123
    }
}
print (car['owner'])