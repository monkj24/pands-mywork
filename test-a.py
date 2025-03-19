
with open("test-a.txt") as f:
    data = f.read()
    print (data)

with open("test-b.txt", "w") as f:
    data = f.write("test b\n")
    print(data)

with open("test-b.txt","w") as f2:
    data =f2.write("another line\n")
    print(data)