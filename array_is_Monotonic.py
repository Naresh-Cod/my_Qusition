
# Check if given array is Monotonic

def monotonic(ls):
    x, y = [], []
    x.extend(ls)
    y.extend(ls)
    x.sort()
    y.sort(reverse=True)
    if (x == ls or y == ls):
        return True
    return False
ls = [9, 7, 6, 4, 3, 1]
print(monotonic(ls))

