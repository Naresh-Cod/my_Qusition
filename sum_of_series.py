# Simple python program to find sum of series

def sum(num):
    sum = 0
    for i in range(1, num+1):
        sum += i * i * i

    return sum
num = 5
print(sum(num))
