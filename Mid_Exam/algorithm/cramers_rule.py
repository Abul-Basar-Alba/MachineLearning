import numpy as np

def cramers_rule(A, b):
    """
    Solve Ax = b using Cramer's Rule
    A : square matrix (n x n)
    b : column vector (n,)
    Returns: solution vector x
    """
    n = len(b)
    det_A = np.linalg.det(A)
    
    if det_A == 0:
        raise ValueError("Determinant is zero, system has no unique solution.")
    
    x = np.zeros(n)
    for i in range(n):
        A_copy = A.copy()
        A_copy[:, i] = b
        det_Ai = np.linalg.det(A_copy)
        x[i] = det_Ai / det_A
    return x

if __name__ == "__main__":
    A = np.array([[2, 1, -1],
                  [-3, -1, 2],
                  [-2, 1, 2]], dtype=float)

    b = np.array([8, -11, -3], dtype=float)

    solution = cramers_rule(A, b)
    print("Solution vector x =", solution)
