# lambda  = arguments: single expression

# multiple line
def sum(a, b):
    return(a + b)
r = sum(10, 20)
print(r)

# single line
s = (lambda a, b: a + b)(10, 20)
# r = s(10, 20)
print(s)

# create a lambda expression to find greater number between two number
p = (lambda a, b: a if a > b else b)(10, 20)
print(p)
