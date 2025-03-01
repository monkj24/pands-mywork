#reads in a string and strips any leading or trailing spaces
# convert the string to lower case
# output the length of the input and output strings

# author Joanna Mnich

rawstring = input("Please enter a string:")
normalisedString = rawString.strip().lower()

lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)

print(f"That String normalised is: {normalisedString}")
print(f"we reduced the input string from {lenghtOfRawString} to
{lenghtOfNormalised} characters")
