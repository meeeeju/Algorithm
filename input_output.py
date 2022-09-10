import sys


N,M=map(int,sys.stdin.readline().split())  #한줄에 있는 정수 2개를 띄어쓰기를 기준으로  입력받을때
N,M=map(int,sys.stdin.readline().split(','))  #한줄에 있는 정수 2개 ,를 기준으로를 입력받을때

print(N,M)


data=input()  #정수를 한줄에 입력받아 리스트로 저장  data='1','2','3','4'
data=input().split()  # 공백 기준으로 나눠서 리스트로 저장
data=map(int,input.split()) #리스트에 있는 모든 배열에 대하여 Int 적용
data=list(map(int,input.split()))
a,b,c = map(int, input().split())  #unpacking 1 2 3을 입력 받았다면 a=1 b=2 c=3
 

a = int(sys.stdin.readline())  #정수 한개 입력받기 
b = sys.stdin.readline().rstrip()  #한줄 단위의 문자열 입력받기
data = list(map(int, sys.stdin.readline().split()))  #여러개의 정수 입력받아 리스트로 저장하기


