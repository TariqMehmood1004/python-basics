
# Metaclass - used to create classes in Python
class MyClassMeta(type):
    pass

class MyClass(metaclass=MyClassMeta):
    pass