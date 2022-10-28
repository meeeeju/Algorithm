from collections import deque
import sys

# input=sys.stdin.readline

# data = list(map(int, sys.stdin.readline().rstrip()))  
# print(data)

# list1=[1,2,3,4,5]
# print(list1[-1])
class Account:
        num_accounts = 0
        def __init__(self, name):
                self.name = name
                Account.num_accounts += 1
        def __del__(self):
                Account.num_accounts -= 1
kim=Account('meeju')

print(kim.name)
print(Account.num_accounts)