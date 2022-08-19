import sys

top=0
answer=""
for j in range(int(sys.stdin.readline())):
    word=list(sys.stdin.readline().rstrip())
    #print(word)

    # if word[0]==')':
    #     print("NO")
    #     continue

    for i in word:
        if i=='(':
            top+=1
        else: 
            top-=1

        if top<0:
            answer="NO"
            break
    if (top!=0):
        print("NO")
    else:
        print("YES")
    top=0


#이런 경우에는 함수를 쓰자,, NO가 되는 경우를 생각해보자, 1. ()는 짝을 이루어야한다. 2. )이 먼저나오는 경우는 )( 틀린 경우다.