'''
    파이썬 내장 함수인 max 로 최대값 찾기
'''
import time

n = int(input("Number of elements: "))
haystack = [k for k in range(n)]

print("Searching for the maximum value...")

ts = time.time()
maximum = max(haystack)
elapsed = time.time() - ts

print(f"Maximum element = {maximum}, Elapsed time = {elapsed}")