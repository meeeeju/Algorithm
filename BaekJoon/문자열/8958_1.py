import sys
input=sys.stdin.readline

N=int(input())

for i in range(N):
    ox=input().rstrip()
    score=0
    ox_weight=0
    for str in ox:
        if str=='O':
            ox_weight=ox_weight+1
            score+=ox_weight
        else:
            ox_weight=0
    print(score)
            