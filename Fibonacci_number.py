# Function for fibonacci number

def fibonacci(num):
    a = 0
    b = 1
    if num < 0:
        print('Incorrect !!!')
    elif num == 0:
        return a
    elif num == 1:
        return b
    else:
        for i in range(2, num):
            c = a + b
            a = b
            b = c
        return b
fi = fibonacci(8)
print(fi)
