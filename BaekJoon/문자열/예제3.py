#유형 3 : 조건에 맞게 재정렬
import sys
input=sys.stdin.readline

data=['1 A','2 B','6 A','2 D','4 B']

data.sort(key=lambda x: (x.split()[1],x.split()[0]))
print(data)