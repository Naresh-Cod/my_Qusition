# linear search
li = [4, 55, 3, 9, 5, 33, 66]
search = int(input("Enter search value: "))
for i in range(len(li)):
    if li[i] == search:
        print(li[i], end=' ')
        print('block num: ', i, 'and value is: ', li[i])
