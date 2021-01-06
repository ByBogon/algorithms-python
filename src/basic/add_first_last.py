'''
    입력으로 주어지는 리스트 x의 첫 원소와 마지막 원소의 합을 리턴하는 함수 solution()을 완성하세요.
'''
def solution(x):
    return x[0] + x[-1]

input_list = [int(x) for x in input().split(' ')]
print(solution(input_list))