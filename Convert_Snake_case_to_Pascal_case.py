


# string input
stri = "Python, programming"

# printing original string
print("Original string: ", stri)

# Convert Snake case to Pascal case
sym = stri.split(", ")
lis = []
for x in sym:
    x = x.title()
    lis.append(x)
res = "".join(lis)

print("Changing String: ", str(res))

