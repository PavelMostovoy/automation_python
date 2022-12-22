class A:
    def __init__(self, value):
        self.value_a = value
    a_property =  1

class B:
    def __init__(self):
        self.value_b = 30
    b_property = 2


class C (list):
    __class__ =  str
    def __init__(self, value):
        # super().__init__()
        # super().__init__(value + 10)
        self.value = value
    value_c = 1.1





inst = C(1)
print(inst.value)

print(isinstance(inst, list))

