
# Sum of multiples of 2 and 5

def number(limit_num):
    sum_value = 0
    for i in range(0, limit_num + 1):
        if i % 2 == 0 or i % 5 == 0:
            sum_value += i
            print(sum_value)
number(10)