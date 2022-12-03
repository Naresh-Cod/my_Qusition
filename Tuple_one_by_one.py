# number sequence

tuple_num = (2, 5, 4, 8, 6, 5)
num = 0
len_num = len(tuple_num)
while True:
    if num == len_num:
        exit()
    print(tuple_num[num])
    num += 1
