# Write a program that will read in the data for the data structure from studentcourses.py file
# reads in a student’s name, 
# then keeps reading in their modules and grades (until the user enters a blank module name),  
# break this up into two parts: 
## a. Just read in the module names until the user enters blank, 
## b. Then read in the grade as well 



# Part 1: Read the student's name
student_name = input("Enter the student's name: ")

# Part 2: Read module names until the user enters a blank module name
modules = []
while True:
    module_name = input("Enter the module name (or leave blank to finish): ").strip()
    if not module_name:  # If the module name is blank, stop reading
        break
    modules.append(module_name)

# Part 3: Read grades for each module
grades = {}
for module in modules:
    grade = input(f"Enter the grade for {module}: ").strip()
    grades[module] = grade

# Part 4: Store the data in a structured format
student_data = {
    "name": student_name,
    "modules": grades
}

# Part 5: Display the student's data
print("\nStudent Data:")
print(f"Name: {student_data['name']}")
print("Modules and Grades:")
for module, grade in student_data["modules"].items():
    print(f"  {module}: {grade}")