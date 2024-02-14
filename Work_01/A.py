import numpy as np
import typing as tp

def matrix_multiplication(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    return np.array(np.sum(A[:, :, None] * B[:, :], axis=1))

A = np.array([[1, 1, 3], [2, 1, 1], [1, 1, 1]])
B = np.array([[1, 1], [2, 1], [1, 1]])

print(matrix_multiplication(A, B))