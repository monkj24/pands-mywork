# a program that puts 10 random numbers into a queue(list), 
# the program should then output all the values in the queue, 
# then take the numbers from the queue one at a time,
#  print it and the current numbers still in the queue. 


import random

# Initialize the queue and parameters
queue = []
numberOfNumbers = 10
rangeTo = 100

# Generate random numbers and add them to the queue
for n in range(0, numberOfNumbers):
    queue.append(random.randint(0, rangeTo))

# Print the initial queue
print(f"Queue is {queue}")

# Process the queue
while len(queue) != 0:
    currentNumber = queue.pop(0)  # Remove the first element from the queue
    print(f"Current Number is {currentNumber} and the queue is {queue}")

# Print final message
print("The queue is now empty")