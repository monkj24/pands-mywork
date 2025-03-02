# more messing with dictionaires
# I am looking at for loops

# Author: Joanna Mnich

car = {
    'make': 'Fiat',
    'model': 'Punto',
    'price': 10000,
    'tags': ['pre-owned', 'Best buy', 'Dealer']
}
# print(car)

for key in car:
    print(key, 'has value', car[key])

for key, value in car.items():
    print (key + 'has value', value)
