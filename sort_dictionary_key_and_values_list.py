


# Sort dictionary key and values list

# initializing dictionary
dic ={'simple': [7, 4, 3],
      'lo': [33, 77, 5],
      'hard': [22, 5]}

# printing original dictionary
print("original dic :" + str(dic))

# using loop + dictionary comprehension
non = dict()
for key in sorted(dic):
    non[key] = sorted(dic[key])

# printing result
print("sorted dic: "+ str(non))
