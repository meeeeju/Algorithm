import sys
input=sys.stdin.readline


N=int(input())
grade_storage=[]
sum=0

for _ in range(N):
    data=input().rstrip()
    for i in range(len(data)):
        str=data[i]
        if str=='O':
            if i==0:
                score=1
                grade_storage.append(score)
                prev=str  
                continue    
            if prev=='O':
                score=grade_storage[-1]+1         
            else:
                score=1      
            grade_storage.append(score)
            prev=str
        if str=='X':
            prev=str
    for score in grade_storage:
        sum+=score
    print(sum)
    sum=0
    grade_storage.clear()






    