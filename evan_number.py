chance = 1
print(": three chance: ")
while chance <= 3:
    value = int(input("Enter evan number: "))
    if value % 2 == 0:
        print("value is evan\n")
        break
    chance += 1
