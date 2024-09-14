import numpy as np

def matrix_multiplication(size):
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    result = np.dot(A, B)
    return result

if __name__ == "__main__":
    print("Performing matrix multiplication")
    result = matrix_multiplication(1000)
    print("Finished matrix multiplication")
