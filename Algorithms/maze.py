# def has_path(maze, start ,end):
#     dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
#     # add
#     queue = []
#     queue.append(start)
#     rr = len(maze)
#     cc = len(maze[0])
#     while queue:
#         point = queue.pop(0)
#         maze[point[0]][point[1]] = 2
#         if point[0] == end[0] and point[1] == end[1]:
#             return True

#         for i in dirs:
#             next_r = point[0] + i[0]
#             next_c = point[1] + i[1]
#             if 0 <= next_r and next_r < rr and 0 <= next_c and next_c < cc:
#                 if maze[next_r][next_c] == 0:
#                     queue.append((next_r,next_c))
#     return False







# def get_shortest_path_length(maze, start, end):
#     dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
#     # add
#     queue = []
#     queue.append(start)
#     rr = len(maze)
#     cc = len(maze[0])
#     while queue:
#         point = queue.pop(0)
#         path_length = point[2]
#         maze[point[0]][point[1]] = 2
#         if point[0] == end[0] and point[1] == end[1]:
#             return path_length

#         for i in dirs:
#             next_r = point[0] + i[0]
#             next_c = point[1] + i[1]
#             if 0 <= next_r and next_r < rr and 0 <= next_c and next_c < cc:
#                 if maze[next_r][next_c] == 0:
#                     queue.append((next_r,next_c))
#     queue.append((next_r, next_c, path_length +1))

# def find_shortest_path(maze, start, end):
#     # add
#     # return path
#     pass

 
# def see_path(maze,path):     #使寻找到的路径可视化
#     for i,p in enumerate(path):
#         if i==0:
#             maze[p[0]][p[1]] ="E"
#         elif i==len(path)-1:
#             maze[p[0]][p[1]]="S"
#         else:
#             maze[p[0]][p[1]] =3
#     print("\n")
#     for r in maze:
#         for c in r:
#             if c==3:
#                 print('\033[0;31m'+"*"+" "+'\033[0m',end="")
#             elif c=="S" or c=="E":
#                 print('\033[0;34m'+c+" " + '\033[0m', end="")
#             # elif c==2:
#             #     print('\033[0;32m'+"#"+" "+'\033[0m',end="")
#             elif c==1:
#                 print('\033[0;;40m'+" "*2+'\033[0m',end="")
#             else:
#                 print(" "*2,end="")
#         print()
 



# maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
#         [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
#         [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
#         [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
#         [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
#         [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
#         [1,1,1,0,0,0,0,0,0,0,0,1,0,1],\
#         [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
#         [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
#         [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
#         [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
#         [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
# start=(1,1)
# end=(10,12)
# result = has_path(maze, start, end)
# print(result) # False


# maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
#         [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
#         [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
#         [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
#         [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
#         [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
#         [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
#         [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
#         [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
#         [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
#         [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
#         [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
# start=(1,1)
# end=(10,12)
# #result = has_path(maze, start, end)
# result = get_shortest_path_length(maze, start, end)
# print(result) # True


# # length = get_shortest_path_length(maze, start, end)
# # print(length)
# # path = find_path(maze,start,end)
# # print(path)
# # see_path(maze, path)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))

