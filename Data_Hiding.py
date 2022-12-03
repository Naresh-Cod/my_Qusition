
class super:
    y = 222 # static variable
    __h = 40 # static, hidden variable

    def f1(self):
        print(super.__h)

super().f1()
print(super.y)
print(super._super__h)

