f = open("demofile.txt")

print(f.read()) #prints the text

f = open("D:\\myfiles\demofile.txt") #creating a path
print(f.read())

#with <expression> as <variable>:
    # Do something with <variable>
with open("demofile.txt") as f:
  print(f.read())

#closing after reading
f = open("demofile.txt")
print(f.readline())
f.close()


#how many chaarcters reader wants to return
with open("demofile.txt") as f:
  print(f.read(5)) #result-> "hello"


#returning a line
with open("demofile.txt") as f:
  print(f.readline())
  print(f.readline()) #prints the first two lines


with open("demofile.txt") as f:
  for x in f:
    print(x)   #printing each line by looping


    