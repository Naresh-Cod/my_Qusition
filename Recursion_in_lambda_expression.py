# functon
def fact(a):
    if(a == 0):
        return 1
    return a * fact(a - 1)
r = fact(5)
print(r)

# lambda
s = lambda a: 1 if a == 0 else a * s(a - 1)
print('factorial is ', s(5))

