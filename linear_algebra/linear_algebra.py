import scipy.linalg as linalg
import numpy as np

if __name__ == '__main__':
    '''
    equations: 
    3x +4y =10
    2x +5y =9
    '''
    a = np.array([[3, 4], [2, 5]])
    b = np.array([10, 9])
    print(f"Solve equation-> {linalg.solve(a, b)}")

    '''
    matrix
    1 , 2 , 3
    4 , 5 , 6
    7 , 8 , 9
    '''
    matrix = np.array([[1, 2, 3], [4, 5, 6], [8, 8, 9]])
    print(f"Determinate -> {linalg.det(matrix)}")
    inverse_mat = linalg.inv(matrix)
    print(f"Inverse -> {inverse_mat}")

    print(f"Inverse matrix product -> {matrix * inverse_mat}")

    eign_value, eign_vector = linalg.eig(matrix)
    print()
    print(eign_value)
    print(eign_vector)
