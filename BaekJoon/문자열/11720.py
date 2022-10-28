import sys
input=sys.stdin.readline


N=int(input())

# data=list(map(int,input().rstrip()))
# sum=0
# for i in data:
#     sum=sum+i
    

# print(sum)


sum1=0
data1=int(input().rstrip())
for _ in range(N):
    sum1+=data1%10
    data1//=10
print(sum1)
