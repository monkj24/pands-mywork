# read in two numbers and multiple them

def readNum(message = "enter a number:"):
    num = False

    while (not num):
        try:
            num = int(input(message))
        except ValueError:    
            print("thas was not a number", end="")   
    return num

num1 = readNum()
num2 = readNum("enter num2: ")

answer = num1 * num2
print(f"answer is {answer}")





