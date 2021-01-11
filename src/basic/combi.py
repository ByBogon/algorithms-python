"""
n개의 서로 다른 원소에서 m개를 택하는 경우의 수
"""
from math import factorial as f


def combi(n, m):
    return f(n) / (f(m) * f(n - m))


"""
재귀적 방법으로.
효율성 측면에서는 n이 커지면 함수가 여러번 호출 됨으로써, 효율적이지 않음.
그러나 사람이 생각하는 방식과 비슷해서 쓸모있는 경우가 많음.
"""


def combi_recursion(n, m):
    if n == m:
        return 1
    elif m == 0:
        return 1
    else:
        return combi_recursion(n - 1, m) + combi_recursion(n - 1, m - 1)