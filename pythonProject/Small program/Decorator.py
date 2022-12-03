# decorator
def decor_result(result_functon):
    def distinction(marks):
        for m in marks:
            if m >= 75:
                print('congrats !!, you have got distinaction')
            else:
                result_functon(marks)
    return distinction
@decor_result
def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print('Fall')
            break
    else:
        print('PASS')

result([50, 60, 15, 96, 66])
#result([50, 60, 75, 90, 66])

def result(marks):
    for m in marks:
        if m >= 33:
            pass
        else:
            print('Fall')
            break
    else:
        print('PASS')
result([50, 60, 70, 80, 44])

# fist 1 logic
def num():
    print("we will use this function")
    print("and will enhance this in decoration")

def decor(fun):
    def inner():
        print("If: befro enhancing function")
        fun()
        print("after enhancing function")
    return inner

hi = decor(num)
hi()

# secend 2 logic
def decor(fun):
    def inner():
        a = fun() + 5
        return a
    return inner

def decor_1(sos):
    def inner_1():
        a = sos() + 5
        return a
    return inner_1

def num():
    return 20

ai = decor(decor_1(num))
print(ai())
