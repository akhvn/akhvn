import numpy as np
import cmath
import math

class MyMath:
    # всё наже - инкапсуляция
    __complex = False
    pi = np.pi

    @classmethod
    def get_nm(cls):
        return cls.__name__

    @staticmethod
    def sin(x):
        return np.sin(x)

    @classmethod
    def get_complex(cls):
        return cls.__complex

    @classmethod
    def sqrt(cls, x):
        if cls.get_complex():  # полиформизм
            result = cmath.sqrt(x)
            return result.real, result.imag
        else:
            if x < 0:
                raise ValueError("Hey, you are working with real valued math!")
            if x >= 0:
                return np.sqrt(x)
          
class MyComplexMath(MyMath):  # наследование
    __complex = True

    @classmethod
    def get_complex(cls):
        return cls.__complex


print(MyMath.sqrt(4))
print(MyComplexMath.sqrt(4))
print(MyComplexMath.sqrt(2j))
print(MyComplexMath.sqrt(-4))
print(MyMath.sqrt(-4))
