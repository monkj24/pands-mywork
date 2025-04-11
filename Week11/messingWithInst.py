# messing with objects

# author Joanna Mnich

class Nameofclass:
    name = ""
    last = ""

    def getfullname(self):

        return self.name + ' ' + self.name
    
inst = Nameofclass()
inst2 = Nameofclass()

inst.name = 'andrew'
inst2.last = 'beatty'
person = inst
print(person.name)

inst.last = "blocks"
print(person.getfullname())

str1 = "blah de blah"
str2 = str1 

str1 += "with the bells on top"

print(str2)