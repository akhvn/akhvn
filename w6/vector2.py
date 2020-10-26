import math
import numpy as np

class Vector(object):
    def __init__(self, *args):
        
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def norm(self):
        return math.sqrt(sum(comp**2 for comp in self))

    def argument(self):
        arg_in_rad = math.acos(Vector(0, 1)*self/self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0] < 0:
            return 360 - arg_in_deg
        else:
            return arg_in_deg

    def normalize(self):
        norm = self.norm()
        normed = tuple(comp/norm for comp in self)
        return Vector(*normed)

    def rotate(self, *args):
        if len(args) == 1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
            # So, if rotate is passed an int or a float...
            if len(self) != 2:
                raise ValueError(
                    "Rotation axis not defined for greater than 2D vector")
            return self._rotate2D(*args)
        elif len(args) == 1:
            matrix = args[0]
            if not all(len(row) == len(v) for row in matrix) or not len(matrix) == len(self):
                raise ValueError(
                    "Rotation matrix must be square and same dimensions as vector")
            return self.matrix_mult(matrix)
    def _rotate2D(self, theta):
        """ Rotate this vector by theta in degrees.

            Returns a new vector.
        """
        theta = math.radians(theta)
        # Just applying the 2D rotation matrix
        dc, ds = math.cos(theta), math.sin(theta)
        x, y = self.values
        x, y = dc*x - ds*y, ds*x + dc*y
        return Vector(x, y)

    def matrix_mult(self, matrix):
        
        if not all(len(row) == len(self) for row in matrix):
            raise ValueError('Matrix must match vector dimensions')

        # Grab a row from the matrix, make it a Vector, take the dot product,
        # and store it as the first component
        product = tuple(Vector(*row)*self for row in matrix)

        return Vector(*product)

    def inner(self, other):
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple(a * other for a in self)
            return Vector(*product)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple(a / other for a in self)
            return Vector(*divided)

    def __add__(self, other):
        added = tuple(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __sub__(self, other):
        subbed = tuple(a - b for a, b in zip(self, other))
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)

class MyVector(Vector):
    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        elif type(args[0]) == str:
            temp = list(map(float, list(args[0].split(','))))
            self.values = temp
        else:
            self.values = args

    def __and__(self, other):
        a = np.array(self)
        b = np.array(other)
        return np.cross(a, b)
'''
a = MyVector(1, 2, 3)
b = MyVector('4, 5, 6')

print(a)
print(b)

print(f'Sum = {a + b}')
print(f'Dot product = {a * b}')
print(f'Cross product = {a & b}')
'''
N = int(input())
vector_list = []
for _ in range(N):
    temp = input()
    temp = ','.join(list(temp.split(' ')))
    vector_list.append(MyVector(temp))

for vector in vector_list:
    mx = MyVector()
    if vector.norm() > mx.norm():
        mx = vector
        
print(mx)
