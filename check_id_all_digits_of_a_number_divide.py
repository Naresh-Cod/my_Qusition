


# Python Program for Check if
# all digits of a number divide it

# Function to check
# the divisibility
# of the number by
# its digit.
def check(n, digit):
    # If the digit divides the

    # else return false.
    return (digit != 0 and n % digit == 0)

# Function to check if
# all digits of n divide
# it or not
def Divide(n):
    temp = n
    while (temp > 0):

        digit = temp % 10
        if ((check(n, digit)) == False):
            return False

        temp = temp // 10
    return True

# Driver function
n = 128

if (Divide(n)):
    print("Yes")

