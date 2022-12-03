
def has(key):
    sum = 0
    for c in key:
        sum += ord(c)
    return sum % 100

for i in range(1, 100):
    keys = 'march ' + str(i)
    if has(keys) == 60:
        print(keys, '=', has(keys))
