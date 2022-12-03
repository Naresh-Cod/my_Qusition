def avg(**n):
    for key, value in n.items():
        return key, '=', value
x = avg(a='hello', b='hi')
print(x)

def avg(**n):
    return n
x = avg(a='hello', b='hi')
print(x)
