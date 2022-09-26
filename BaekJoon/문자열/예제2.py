#문자열 뒤집기
#이번 유형은 리스트 내부에 있는 문자열을 뒤집는 방법을 물어보는 것이다.
import sys
input=sys.stdin.readline

def reverseString(str):
    str.reverse()


def reverseStringSlicing(str):
    str=str[::-1]
    #만약에 오류가 나면 str[:]=str[::-1]


def reverseStringTopointer(str):
    left_idx, right_idx = 0, len(str)-1
    while left_idx <right_idx:
        str[left_idx],str[right_idx]=str[right_idx],str[left_idx]
        left_idx +=1
        right_idx -=1

    
a=list(input().rstrip())
print(a)
reverseString(a)
print(a)
reverseStringSlicing(a)
print(a)
reverseStringTopointer(a)
print(a)