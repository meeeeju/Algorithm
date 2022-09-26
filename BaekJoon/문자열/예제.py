#유형 1 회문(Palindrome)
from curses.ascii import isalnum
import collections
import sys

input=sys.stdin.readline


#전처리
# isalnum() : 영문자 , 숫자여부를 판별하여 영문자와 숫자가 아닌경우, false를 return
# lower() : 영어 알파벳 모두 소문자로 변환한다.
def inPlindrome(str):
    list_str=[]
    for char in str:
        if char.isalnum():
            list_str.append(char.lower())


def isPalindromeIndex(str):
    for i in range(len(str)//2):
        if str[i]==str[-i-1]:
            continue
        else:
            print("회문이 아닙니다.")
            return
    print("회문입니다.")
    

def isPalindromeSlicing(str):
    if str[:]==str[::-1]:  # str==str[::-1]
        print("회문이다")
    else:
        print("회문이 아닙니다.")

#Deque를 활용한 회문 전처리를 곁들인
def isPalindromeDequeue(str):
    deq=collections.deque()
    for char in str:
        if char.isalnum():
            deq.append(char.lower())
    

    while len(deq<1):
        if deq.popleft() != deq.pop():
            print("회문이 아닙니다")
            return
    print("회문입니다.")
        


isPalindromeIndex(input().rstrip())
isPalindromeSlicing(input().rstrip())
