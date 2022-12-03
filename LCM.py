# L.C.M of two numbers

a1 = int(input("Enter first num: "))
a2 = int(input("Enter sec. num: "))

greater = a1 if a1 > a2 else a2

while True:
    if greater % a1 == 0 and greater % a2 == 0:
        lcm = greater
        break
    greater += 1
print("LCM OF", a1, "AND", a2, '=', greater)
