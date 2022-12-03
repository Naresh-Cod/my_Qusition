
# Python program to find cumulative sum of a list

list = [12, 55, 66, 33, 77, 44]

new_l = []
num = 0
for i in range(0, len(list)):
    num += list[i]
    new_l.append(num)

print(new_l)


