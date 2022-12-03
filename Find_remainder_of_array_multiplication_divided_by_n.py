# to use reduce function import reduce from functools
from functools import reduce

def find_remainder(arr, n):
    sum_1 = reduce(lambda x, y: x * y, arr)
    remainder = sum_1 % n
    print(remainder)

arr = [100, 10, 5, 25, 35, 14]
n = 11
find_remainder(arr, n)


# Find remainder of arry multiplication
# divided by n

def find_remainder(arr, lens, a):
    num = 1
    # find the individual remainder

    for i in range(lens):
        num = (num * (arr[i] % a)) % a
    return num % a
# Driven code
arr = [300, 50, 200, 300]

print(find_remainder(arr, len(arr), 11))


