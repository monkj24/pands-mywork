# this program is to show how you can use try except


#filename ='data.txt'
import sys

#print (sys.argv)
try:
    filename = sys.argv[1]
    print(filename)
    with open(filename) as fp:
        print(fp.read())

except IndexError as ie:
    print("please enter the filename as an argument")
    #print(ie)
except FileNotFoundError:
    print(f"fie {filename} not found, please enter a filename that excist")
