# Armstrong number
num = int(input("Enter number: "))
s = num
length = len(str(num))
p = 0
while num != 0:
    r = num % 10
    p += r ** length
    num = num // 10

if num == p:
    print("Value is Armstrong number: ", p)
else:
    print("Value is not Armstrong number: ", p)
