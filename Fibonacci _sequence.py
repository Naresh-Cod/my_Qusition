# Program to the Fibonacci sequence
temp = int(input("How many terms: "))
# first two terms
p1, p2 = 0, 1
count = 0
#check if the number of terms is valid
if temp <= 0:
    print("Please enter a positive integer")
elif temp == 1:
    print("Fibonacci sequence upto", temp)
    print(p1)
# generate fibonacci sequence
else:
    print("Fibonacci sequence: ")
    while count < temp:
        print(p1, end=" ")
        sos = p1 + p2
        #update values
        p1 = p2
        p2 = sos
        count += 1
