import sys
sys.path.append("../")
from ex02.vector import Vector

class Matrix:
	def __init__(self, array: list):
		try:
			self.array = array.copy()
			array_len = -1
			for i in range(len(self.array)):
				if isinstance(self.array[i], list) == False:
					raise
				self.array[i] = list(map(lambda x: float(x), self.array[i]))
				if array_len != -1 and array_len != len(self.array[i]):
					raise
				array_len = len(self.array[i])
		except Exception:
			print("error", array)

	def shape(self):
		x_len = len(self.array)
		y_len = len(self.array[0])
		return (x_len, y_len)

	def data(self, data):
		matrix = Matrix(data)
		return tuple(matrix)

	def _isComputable(self, data1, data2):
		shape1 = -1
		shape2 = -2
		if isinstance(data1, Matrix):
			shape1 = data1.shape()
		elif isinstance(data1, Vector):
			shape1 = (len(data1.val), 1)
		if isinstance(data2, Matrix):
			shape2 = data2.shape()
		elif isinstance(data2, Vector):
			shape2 = (len(data2.val), 1)
		if isinstance(data1, int) or isinstance(data2, int):
			return True
		if shape1[1] == shape2[0]:
			return True
		else:
			return False

	def __add__(self, other):
		if not (isinstance(other, Matrix) or isinstance(other, int)):
			print("not Computable")
			return 0
		if self._isComputable(self, other) == False:
			print("not Computable")
			return 0
		rtv = []
		if isinstance(other, int):
			for line in self.array:
				rtv.append(list(map(lambda x: x + other, line)))
			return rtv
		elif isinstance(other, Matrix):
			for i in range(self.shape()[0]):
				rtv_line = []
				for j in range(self.shape()[1]):
					rtv_line.append(self.array[i][j] + other.array[i][j])
				rtv.append(rtv_line)
		return rtv

	def __radd__(self, other):
		return (self.__add__(other))

	def __sub__(self, other):
		if not (isinstance(other, Matrix) or isinstance(other, int)):
			print("not Computable")
			return 0
		if self._isComputable(self, other) == False:
			print("not Computable")
			return 0
		rtv = []
		if isinstance(other, int):
			for line in self.array:
				rtv.append(list(map(lambda x: x - other, line)))
			return rtv
		elif isinstance(other, Matrix):
			for i in range(self.shape()[0]):
				rtv_line = []
				for j in range(self.shape()[1]):
					rtv_line.append(self.array[i][j] - other.array[i][j])
				rtv.append(rtv_line)
		return rtv

	def __rsub__(self, other):
		if not (isinstance(other, Matrix) or isinstance(other, int)):
			print("not Computable")
			return 0
		if self._isComputable(self, other) == False:
			print("not Computable")
			return 0
		rtv = []
		if isinstance(other, int):
			for line in self.array:
				rtv.append(list(map(lambda x: other - x, line)))
			return rtv
		elif isinstance(other, Matrix):
			for i in range(self.shape()[0]):
				rtv_line = []
				for j in range(self.shape()[1]):
					rtv_line.append(other.array[i][j] - self.array[i][j])
				rtv.append(rtv_line)
		return rtv

	def __truediv__(self, other):
		if not (isinstance(other, int)):
			print("not Computable")
			return 0
		if self._isComputable(self, other) == False:
			print("not Computable")
			return 0
		rtv = []
		if isinstance(other, int):
			for line in self.array:
				rtv.append(list(map(lambda x: x / other, line)))
			return rtv
		return rtv

	def __rtruediv__(self, other):
		if not (isinstance(other, int)):
			print("not Computable")
			return 0
		if self._isComputable(self, other) == False:
			print("not Computable")
			return 0
		rtv = []
		if isinstance(other, int):
			for line in self.array:
				rtv.append(list(map(lambda x: other / x, line)))
			return rtv
		return rtv

	def __mul__(self, other):
		if not (isinstance(other, Matrix) or isinstance(other, int) or isinstance(other, Vector)):
			print("not Computable")
			return 0
		if self._isComputable(self, other) == False:
			print("not Computable")
			return 0
		rtv = []
		if isinstance(other, int):
			for line in self.array:
				rtv.append(list(map(lambda x: x * other, line)))
			return rtv
		elif (isinstance(other, Vector)):
			for line in self.array:
				sum = 0
				for val1, val2 in zip(line, other.val):
					sum += val1 * val2
				rtv.append(sum)
			return rtv
		elif isinstance(other, Matrix):
			for i in range(self.shape()[0]):
				rtv_line = []
				for j in range(self.shape()[1]):
					sum = 0
					for k in range(self.shape()[0]):
						sum += self.array[i][k] * other.array[k][j]
					rtv_line.append(sum)
				rtv.append(rtv_line)
		return rtv

	def __rmul__(self, other):
		return (self.__mul__(other))

	def __str__(self):
		return "(Matrix " + str(self.array) + ")"
