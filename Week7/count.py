import os.path 
FILENAME = "count.txt" 
if not os.path.isfile(FILENAME): 
    print ("File does not exist") 
#initialise file here 
   

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return  readNumber


def writeNumber(number):
    with open(FILENAME, "wt") as f:
        # write takes a string so we need to convert
        f.write(str(number))

#test it
num = readNumber()
num += 1
print(f"we have run this program {num} times")
writeNumber(num)
