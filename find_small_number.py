# Find small number

a = int(input("Enter the value a : "))
b = int(input("Enter the value b : "))
c = int(input("Enter the value c : "))

if a <= b and a <= c:
    print("a is small")
elif b <= a and b <= c:
    print("b is small")
elif c <= a and c <= b:
    print("c is small")
