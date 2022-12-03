
# Return the sum of square of
# first n natural numbers

def sqr(num):
    # add to sum
    sum = 0
    for i in range(1, num + 1):
        sum = sum + (i * i)
    return sum

# Driven program
num = 12
print(sqr(num))

