students= []
def readModules ():
    return []

def doAdd(students):
    currentStudent = {}
    currentStudent["name"]=input("enter name :")
    currentStudent["modules"]= readModules()

    students.append(currentStudent)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ") .strip()

    while moduleName !="":
        module = {}
        module["name"]= moduleName

        module["grade"]=int(input("\t\tEnter grade:"))
        modules.append(module)
        #now read the next module name
        moduleName = input("\tEnter next module name (blank to quit):") .strip()

    return modules    

# test
doAdd(students)

doAdd(students)
print(students)