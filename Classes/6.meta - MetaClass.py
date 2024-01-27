
class Meta(type):
    def __new__(cls, name, bases, dct):
        for attr, val in dct.items():
            if callable(val):
                dct[attr] = staticmethod(val)
        return super().__new__(cls, name, bases, dct)

class Math(metaclass=Meta):
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b
    
print(Math.add(1, 2))
print(Math.subtract(2, 1))
