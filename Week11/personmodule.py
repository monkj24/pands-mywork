# demonstration of a module

#Author Joanna Mnich

import datetime as dt
def gethealthdata(person):
    print("get health data:", person['firstname'])


def displayperson(person):
    print(person)
'''
if __name__ == '__main__':
    person = {
       'firstname': 'andrew',
       'lastname' : 'beatty',
       'dob' : dt.date(2010,1,1),
       'height' : 180,
       'width' : 100
}
displayperson(person)
gethealthdata(person)
'''