# swap first and last element of a list
# swap function create
def swap(value):

    temp = value[-1], value[0]
    # temp value print (24, 12)
    value[0], value[-1] = temp
    return value

num = [10, 5, 3, 27, 66, 30]
print(num)
print("Swap first and last element")
print(swap(num))
