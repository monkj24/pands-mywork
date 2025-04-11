# messing with init

# Author: Joanna Mnich

class Person:
    def __init__(self, first='', last=''):
        self.firstname = first
        self.lastname = last

    def fullName(self):
        if hasattr(self, 'middlename'):
            return self.firstname + ' ' + self.middlename + ' ' + self.lastname
        return self.firstname + ' ' + self.lastname

    def addmiddlename(self, middlename):
        self.middlename = middlename

    def __str__(self):
        return self.fullName()

if __name__ == '__main__':
    person1 = Person('Joanna', 'Mnich')
    print(person1.firstname)
    print(person1.fullName())

    person1.addmiddlename("Joe")
    print(person1)
