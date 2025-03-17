# Messing with JSON
# This program is to demonstrate storing data ina json format

#Author Joanna Mnich

import json

electricBill = {
    'name': 'Andrew',
    'amount' :'9999'
}

with open("storeData.json", "wt") as f:
    json.dump(electricBill, f) # write the dictonary