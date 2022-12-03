# Python Program for compound interest

principle = 1248 # principle amount
time = 5 # time
rate = 3.5 # rate

# calculates the compound interest
amount = principle * (1 + (rate / 100)) ** time
ci = amount - principle

# interest value
print("Compound Interest is: ", ci)

