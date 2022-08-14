import sys

top=0
for j in range(int(sys.stdin.readline())):
    word=list(sys.stdin.readline())
    #print(word)
    for i in word:
        if i=='(':
            top+=1
        elif i==')':
            top-=1
        elif i=='\n':
            if top != 0:
                print("NO")
            else : 
                print("YES")
    top=0



        
        
       
        
