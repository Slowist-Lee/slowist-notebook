# import numpy as np

# def solve_linear_system(A, B):
#     """
#     解三元一次方程组 AX = B

#     :param A: 系数矩阵，形状为 (3, 3)
#     :param B: 常数项向量，形状为 (3,)
#     :return: 解向量，形状为 (3,)
#     """
#     try:
#         # 使用 numpy 的线性代数求解方法
#         X = np.linalg.solve(A, B)
#         return X
#     except np.linalg.LinAlgError:
#         return "方程组无唯一解"

# # 示例
# A = np.array([
#     [209, 206, 121],
#     [44, 218, 101],
#     [181, 27, 184]
# ])

# B = np.array([65, 65, 65])

# solution = solve_linear_system(A, B)
# print("解是:", solution)

import sympy as sp
import numpy as np


def solve_linear_system_fractional(A, B):
    """
    解三元一次方程组 AX = B，并保留分数形式

    :param A: 系数矩阵，形状为 (3, 3)
    :param B: 常数项向量，形状为 (3,)
    :return: 解向量，形状为 (3,)
    """
    # 将 numpy 数组转换为 sympy 矩阵
    A_sym = sp.Matrix(A)
    B_sym = sp.Matrix(B)

    # 使用 sympy 的求解方法
    try:
        solution = A_sym.LUsolve(B_sym)
        return solution
    except:
        return "方程组无唯一解"

A = np.array([
    [209, 206, 121],
    [44, 218, 101],
    [181, 27, 184]
])

B = np.array([65, 65, 65])


solution = solve_linear_system_fractional(A, B)
print("解是:")
print(solution)

