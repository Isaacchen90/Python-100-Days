class A:
    def __init__(self,a,b) -> int:
        self.ga = a
        self.gb = b
    def i(self):
        return 'hello world!'
    f = 100
test_A = A(89,90)
print(test_A.ga)
test_A.ga = 900
print(test_A.__dict__)
print(test_A.ga)
print(test_A.__doc__)

class B(A):
    def __init__(self, a, b) -> int:
        super().__init__(a, b)
    def i(self):
        return super().i()
test_B = B(400,300)
print(test_B.__dict__)