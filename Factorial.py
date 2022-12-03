# This program calculates the factorial of the input number using recursion including explanation.

def fact(n):
    if n == 1:
        return n
    else:
# recursion
        return n*fact(n-1)
num = int(input("Enter a whole number to find Factorial: "))

if num < 0:
    print("Factorial can’t be calculated for negative number")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of", num, "is", fact(num))


class Test:
    def __init__(self, x):
        self.a = x

    def get_data(self):
        print('some code to fetch data from databas')

    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
t1 = Test(5)
t1.f2()
t1.f1()
def new_get_data(self):
    print("Some code  to fetch data from test")
Test.get_data = new_get_data
print("After monkey patching ")


