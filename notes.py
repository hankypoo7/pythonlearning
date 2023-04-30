import fileinput

print("hello")

currentNumber = 0

for line in fileinput.input():
    print("you entered " + line)
    print("hi")
    print(currentNumber)
    currentNumber = currentNumber + 1
