import numpy as np
import typing as tp

def find_nearest_points(A: np.ndarray, B: np.ndarray, k: int) -> np.ndarray:    
    return np.argsort(np.sqrt(np.sum(B ** 2, axis=1)[:, np.newaxis] - 2 * np.sum(B[:, :, None] * A.T[:, :], axis=1) + np.sum(A ** 2, axis=1)), axis=1)[:, :k] + 1

A = np.array([
    [0, 0],
    [1, 0],
    [2, 0]
])

B = np.array([
    [0, 1],
    [2, 1]
])

print(find_nearest_points(A, B, 2))