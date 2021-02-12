class Vector:
    def __init__(self, val: list):
        self.val = val

    def _calc(self, formula, x, y):
        rtv = []
        if (type(y) is Vector):
            if len(x) != len(y.val):
                print("error")
                return (None)
            rtv = list(map(formula, x, y.val))
        elif (type(y) is int):
            rtv = list(map(formula, x, [y]*len(x)))
        return (rtv)

    def __add__(self, other):
        return self._calc(lambda x, y: x + y, self.val, other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self._calc(lambda x, y: x - y, self.val, other)

    def __rsub__(self, other):
        return self._calc(lambda x, y: y - x, self.val, other)

    def __truediv__(self, other):
        return self._calc(lambda x, y: x * y, self.val, other)

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __mul__(self, other):
        return self._calc(lambda x, y: x / y, self.val, other)

    def __rmul__(self, other):
        return self._calc(lambda x, y: y / x, self.val, other)

    def __str__(self):
        return "(Vector " + str(self.val) + ")"

    def __repr__(self):
        return self.__str__
