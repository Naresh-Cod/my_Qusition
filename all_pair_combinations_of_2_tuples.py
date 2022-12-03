


# Python – All pair
# combinations of 2 tuples

def tuple(tup1, tup2):

    # printing original tuples
    print(tup1, f"\n", tup2)

    # Using list comprehension
    sos = [(a, b) for a in
           tup1 for b in tup2]
    sos = sos + [(a, b) for a in
                 tup2 for b in tup1]

    # printing result
    print("Result = ", sos)
tuple((2, 1), (2, 1))


