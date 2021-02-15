from matrix import Matrix
import sys
sys.path.append("../")
from ex02.vector import Vector


def test_init_matrix(data):
	print(data)
	try:
		matrix = Matrix(data)
		print(matrix)
	except:
		print("error: ", data)
	print(data, end="\n\n")

def test_add_matrix(data1, data2):
	ans = data1 + data2
	print(ans)


def test_sub_matrix(data1, data2):
	ans = data1 - data2
	print(ans)

def test_truediv_matrix(data1, data2):
	ans = data1 / data2
	print(ans)
	
def test_mul_matrix(data1, data2):
	ans = data1 * data2
	print(ans)

if __name__ == '__main__':
	"""
	matrix = Matrix([[1, 2, 2], [2, 3]])
	matrix = Matrix(1)
	matrix = Matrix([1])
	matrix = Matrix([[1, "2"], [2, 3]])
	matrix = Matrix([[1, 2], [2, 3]])
	matrix = Matrix([[1, 2], [2, 3]])

	print(matrix)
	"""

#	test_init_matrix([[1, 2], [2, 3]])
#	test_init_matrix([[1, 2, 2], [2, 3]])
#	test_init_matrix(1)
#	test_init_matrix([2])
#	test_init_matrix([["1", "3"], ["1", "3"]])
#	test_init_matrix([[1, 2]])

#	test_add_matrix(Matrix([[2, 3], [1, 2]]), Matrix([[6, 7], [3, 1]]))
#	test_add_matrix(Matrix([[6, 7], [3, 1]]), Matrix([[2, 3], [1, 2]]))
#	test_add_matrix(Matrix([[2, 3], [1, 2]]), 2)
#	test_add_matrix(2, Matrix([[2, 3], [1, 2]]))
#	test_add_matrix(Matrix([[2, 3], [1, 2]]), Vector([2, 3]))

#	test_sub_matrix(Matrix([[2, 3], [1, 2]]), Matrix([[6, 7], [3, 1]]))
#	test_sub_matrix(Matrix([[6, 7], [3, 1]]), Matrix([[2, 3], [1, 2]]))
#	test_sub_matrix(Matrix([[2, 3], [1, 2]]), 2)
#	test_sub_matrix(2, Matrix([[2, 3], [1, 2]]))
#	test_sub_matrix(Matrix([[2, 3], [1, 2]]), Vector([2, 3]))

#	test_truediv_matrix(Matrix([[2, 3], [1, 2]]), 2)
#	test_truediv_matrix(2, Matrix([[2, 3], [1, 2]]))

	test_mul_matrix(Matrix([[2, 3], [1, 2]]), Matrix([[6, 7], [3, 1]]))
	test_mul_matrix(Matrix([[6, 7], [3, 1]]), Matrix([[2, 3], [1, 2]]))
	test_mul_matrix(Matrix([[2, 3], [1, 2]]), 2)
	test_mul_matrix(2, Matrix([[2, 3], [1, 2]]))
	test_mul_matrix(Matrix([[2, 3], [1, 2]]), Vector([2, 3]))

#	test_add_matrix([[2, 3], [1, 2]], 1)
