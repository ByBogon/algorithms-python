"""
재귀적 이진 탐색
"""

# L = list, x = target, lower = index of the end of left, right = index of the end of right
def bin_search(L, x, l, u):
    if (L[0] > x) or (L[-1] < x) or (u < l):
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        print(f"x is lower than mid: {L}")
        return bin_search(L=L, x=x, l=l, u=mid - 1)
    else:
        print(f"x is higher than mid: {L}")
        return bin_search(L=L, x=x, l=mid + 1, u=u)


L = [1, 2, 3, 5, 6, 7, 8, 9, 11, 15]
x = 4
l = 0
u = len(L) - 1
L1 = [2, 5, 7, 9, 11]
x1 = 4
l1 = 0
u1 = len(L1) - 1
print(bin_search(L=L, x=x, l=l, u=u))
