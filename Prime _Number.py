# Program to check prime or not
numm = int(input("Enter a number: "))
# define a flag variable
ton = False
# prime numbers are greater then 1
if numm > 1:
    for i in range(2, numm):
        if (numm % i) == 0:
            ton = True
            break
# check if flag is True
if ton:
    print(numm, "Is not a prime")
else:
    print(numm, "Is a prime number")
