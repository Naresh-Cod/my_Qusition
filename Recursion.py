# sum of n natural number
    # easy coding
    # easy to read/understandable

def sum(n):
    if (n == 1):
        return 1
    else:
        return n + sum(n - 1)
a = sum(5)
print(a)

r = 0
for i in range(6):
    print(r, '+=', i)
    r += i
print(r)

p = 0
n = int(input('Enter value: '))
while (n >= 1):
    p += n
    n = n - 1
print(p)
