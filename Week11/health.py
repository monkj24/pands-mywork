# use person module

#Author joanna Mnich


import datetime as dt
from personmodule import *

person = {
    'firstname': 'andrew',
    'lastname': 'beatty',
    'dob': dt.date(2010, 1, 1),
    'height': 180,
    'width': 100
}

displayperson(person)
gethealthdata(person)
