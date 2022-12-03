max = int(input("Enter max number: "))

odd_number = []

for i in range(1, max):
    if i % 2 == 1:
        odd_number.append(i)

print('Odd numbers: ', odd_number)
