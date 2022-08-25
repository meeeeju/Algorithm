def counting(count):
#     global queue,answer
#     while(queue):
#         if (len(queue)<count):
#             while(queue):
#                 if(len(queue)==1):
#                     answer=answer+f'{queue.popleft()}'+'>'
#                 else:
#                     answer=answer+f'{queue.popleft()}'+', '

#             break
#         else:
#             for j in range(1,count+1):
#                 if (j<count):
#                     queue.append(queue.popleft())
#                 else:
#                     answer=answer+f'{queue.popleft()}'+', '


# def reverse():
#     global queue,answer
#     while(queue):
#         if(len(queue)==1):
#             answer=answer+f'{queue.pop()}'+'>'
#         else:
#             answer=answer+f'{queue.pop()}'+', '