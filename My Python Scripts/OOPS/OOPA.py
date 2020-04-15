# class cse:
#     pass

class details:
    d = []
    def __init__(self,rno,m1,m2,m3):
        self.rno = rno
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        details.d.append(self)
    def getrno(self):
        return self.rno    
    def getm1(self):
        return self.m1
    def show(self):
        for o in details.d:
            print(o.rno, o.m1, o.m2, o.m3)
    def show2():
        key = None
        for k in details.d:
            if not key or len(k)>len(key):
                key = k
            print(key.show())
        



# =============================================================================
# runfile('/home/prasadm/Desktop/My Python Scripts/OOPS/OOPA.py', wdir='/home/prasadm/Desktop/My Python Scripts/OOPS')
# 
# dir(cse)
# Out[3]: 
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__']
# 
# cse.__class__
# Out[4]: type
# 
# cse.__class__.__base__
# Out[5]: object
# 
# 	cse.
#   File "<ipython-input-6-1891e561a4d0>", line 1
#     cse.
#         ^
# SyntaxError: invalid syntax
# 
# 
# 
# 
# 	cse.__dict__
# Out[7]: 
# mappingproxy({'__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'cse' objects>,
#               '__weakref__': <attribute '__weakref__' of 'cse' objects>,
#               '__doc__': None})
# 
# 	cse.__dict__()
# Traceback (most recent call last):
# 
#   File "<ipython-input-8-b98c64bda051>", line 1, in <module>
#     cse.__dict__()
# 
# TypeError: 'mappingproxy' object is not callable
# 
# 
# 
# 
# 	cse.__dict__
# Out[9]: 
# mappingproxy({'__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'cse' objects>,
#               '__weakref__': <attribute '__weakref__' of 'cse' objects>,
#               '__doc__': None})
# 
# cse.clg='AEC'
# 
# cse.__dict__
# Out[11]: 
# mappingproxy({'__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'cse' objects>,
#               '__weakref__': <attribute '__weakref__' of 'cse' objects>,
#               '__doc__': None,
#               'clg': 'AEC'})
# 
# a = cse()
# 
# a
# Out[13]: <__main__.cse at 0x7efeeffc7dd0>
# 
# a.__dict__
# Out[14]: {}
# 
# cse.__dict__
# Out[15]: 
# mappingproxy({'__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'cse' objects>,
#               '__weakref__': <attribute '__weakref__' of 'cse' objects>,
#               '__doc__': None,
#               'clg': 'AEC'})
# 
# dir(object)
# Out[16]: 
# ['__class__',
#  '__delattr__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__']
# 
# object.__init__?
# Signature:      object.__init__(self, /, *args, **kwargs)
# Call signature: object.__init__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__init__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Initialize self.  See help(type(self)) for accurate signature.
# 
# object.__new__?
# Signature: object.__new__(*args, **kwargs)
# Docstring: Create and return a new object.  See help(type) for accurate signature.
# Type:      builtin_function_or_method
# 
# object.__str__?
# Signature:      object.__str__(self, /)
# Call signature: object.__str__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__str__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return str(self).
# 
# object.__repr__?
# Signature:      object.__repr__(self, /)
# Call signature: object.__repr__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__repr__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return repr(self).
# 
# object.__eq__?
# Signature:      object.__eq__(self, value, /)
# Call signature: object.__eq__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__eq__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return self==value.
# 
# object.__le__?
# Signature:      object.__le__(self, value, /)
# Call signature: object.__le__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__le__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return self<=value.
# 
# object.__lt__?
# Signature:      object.__lt__(self, value, /)
# Call signature: object.__lt__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__lt__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return self<value.
# 
# object.__gt__?
# Signature:      object.__gt__(self, value, /)
# Call signature: object.__gt__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__gt__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return self>value.
# 
# object.__ge__?
# Signature:      object.__ge__(self, value, /)
# Call signature: object.__ge__(*args, **kwargs)
# Type:           wrapper_descriptor
# String form:    <slot wrapper '__ge__' of 'object' objects>
# Namespace:      Python builtin
# Docstring:      Return self>=value.
# 
# class add:
#   File "<ipython-input-26-e65482c86a20>", line 1
#     class add:
#               ^
# SyntaxError: unexpected EOF while parsing
# 
# 
# 
# 
# class add:
#     def __init__(self,a,b):
#         self.one = a
#         self.two = b
#     def addmem(self):
#         return self.one +self.two
#     def display(self):
#         print(self.one, self.two)
#         
# 
# obj = o
# Traceback (most recent call last):
# 
#   File "<ipython-input-28-cecc09e813e7>", line 1, in <module>
#     obj = o
# 
# NameError: name 'o' is not defined
# 
# 
# 
# 
# obj = add()
# Traceback (most recent call last):
# 
#   File "<ipython-input-29-9a993833061b>", line 1, in <module>
#     obj = add()
# 
# TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
# 
# 
# 
# 
# obj = add(10, 20)
# 
# obj.__dict__
# Out[31]: {'one': 10, 'two': 20}
# 
# class add:
#     def __init__(self):
#         self.one, self.two = 0, 0
#     def __init__(self,a,b):
#         self.one = a
#         self.two = b
#     def addmem(self):
#         return self.one +self.two
#     def display(self):
#         print(self.one, self.two)
#         
# 
# obj = add()
# Traceback (most recent call last):
# 
#   File "<ipython-input-33-9a993833061b>", line 1, in <module>
#     obj = add()
# 
# TypeError: __init__() missing 2 required positional arguments: 'a' and 'b'
# 
# 
# 
# 
# obj = add(10, 20)
# 
# obj.__dict__
# Out[35]: {'one': 10, 'two': 20}
# 
# obj.addmem()
# Out[36]: 30
# 
# obj.display()
# 10 20
# 
# class add:
#     def __init__(self):
#         self.one, self.two = 0, 0
#     def __init__(self,a,b):
#         print('object being initialized')
#         self.one = a
#         self.two = b
#     def addmem(self):
#         return self.one +self.two
#     def display(self):
#         print(self.one, self.two)
#         
# 
# obj = add(10, 20)
# object being initialized
# 
# obj.one
# Out[40]: 10
# 
# obj.two
# Out[41]: 20
# 
# obj.__dict__
# Out[42]: {'one': 10, 'two': 20}
# 
# class add:
#     def __init__(self):
#         self.one, self.two = 0, 0
#     def __init__(self,a,b):
#         print('object being initialized...')
#         self.one = a
#         self.two = b
#     def addmem(self):
#         return self.one +self.two
#     def display(self):
#         print(self.one, self.two)
#     def setiv(self,a,b):
#         self.a = a
#         self.b = b
#         
# 
# obj = add(10, 20)
# object being initialized...
# 
# a.display()
# Traceback (most recent call last):
# 
#   File "<ipython-input-45-f7c7c41098f4>", line 1, in <module>
#     a.display()
# 
# AttributeError: 'cse' object has no attribute 'display'
# 
# 
# 
# 
# obj.display()
# 10 20
# 
# class add:
#     def __init__(self):
#         self.one, self.two = 0, 0
#     def __init__(self,a,b):
#         print('object being initialized...')
#         self.one = a
#         self.two = b
#     def addmem(self):
#         return self.one +self.two
#     def display(self):
#         print(self.one, self.two)
#     def setiv(self,a,b):
#         self.one = a
#         self.two = b
#         
# 
# obj.__dict__
# Out[48]: {'one': 10, 'two': 20}
# 
# obj.setiv(10,20)
# 
# obj.__dict__
# Out[50]: {'one': 10, 'two': 20, 'a': 10, 'b': 20}
# 
# obj = add(10, 20)
# object being initialized...
# 
# obj.setiv(310,410)
# 
# obj.__dict__
# Out[53]: {'one': 310, 'two': 410}
# 
# dir(obj)
# Out[54]: 
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'addmem',
#  'display',
#  'one',
#  'setiv',
#  'two']
# 
# dir(add)
# Out[55]: 
# ['__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__eq__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  'addmem',
#  'display',
#  'setiv']
# 
# a=1
# =============================================================================
