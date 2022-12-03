


# Python program to find
# the sum of all items in a dictionary

def sum(dic):
    sum = 0
    for i in dic.values():
        sum = sum + i

    return sum

# Driver function
dict = {'a': 200, 'b': 500, 'c': 199}
print("Sum value: ", sum(dict))
