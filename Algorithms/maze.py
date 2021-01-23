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

import copy

def has_path(maze_input, start ,end):
    maze = copy.deepcopy(maze_input)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    # add
    queue = []
    queue.insert(0, start)
    maze_height = len(maze)
    maze_width = len(maze[0])
    while queue:
        # print(queue)
        # 走这个点
        curr = queue.pop()
        # 看看是不是终点
        if curr[0] == end[0] and curr[1] == end[1]:
            return True
        for _, dir in enumerate(dirs):
            next_r = curr[0] + dir[0]
            next_c = curr[1] + dir[1]
            if (0 <= next_r and next_r < maze_height
                and 0 <= next_c and next_c < maze_width
                    and maze[next_r][next_c] == 0):
                queue.insert(0, (next_r, next_c))
                # 这些点未来必然要走，做个标记
                maze[curr[0]][curr[1]] = 2

    return False



def get_shortest_path_length(maze_input, start, end):
    maze = copy.deepcopy(maze_input)
    # print(maze)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    queue = []
    start_tuple = (start[0], start[1], 1) # start row, start column, start path length
    queue.insert(0, start_tuple)
    maze_height = len(maze)
    maze_width = len(maze[0])
    while queue:
        # print(queue)
        # 走这个点
        curr = queue.pop()
        # 看看是不是终点
        if curr[0] == end[0] and curr[1] == end[1]:
            return curr[2]
        for _, dir in enumerate(dirs):
            next_r = curr[0] + dir[0]
            next_c = curr[1] + dir[1]
            if (0 <= next_r and next_r < maze_height
                and 0 <= next_c and next_c < maze_width
                    and maze[next_r][next_c] == 0):
                queue.insert(0, (next_r, next_c, curr[2]+1))
                # 这些点未来必然要走，做个标记
                maze[curr[0]][curr[1]] = 2
    return -1


def get_shortest_path_length2(maze_input, start, end):
    maze = copy.deepcopy(maze_input)
    # print(maze)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    queue = []
    queue.insert(0, start)
    maze_height = len(maze)
    maze_width = len(maze[0])
    level = 0
    while queue:
        level += 1
        queue_length = len(queue)
        for _ in range(queue_length):
            # 走这个点
            curr = queue.pop()
            # 看看是不是终点
            if curr[0] == end[0] and curr[1] == end[1]:
                return level
            for _, dir in enumerate(dirs):
                next_r = curr[0] + dir[0]
                next_c = curr[1] + dir[1]
                if (0 <= next_r and next_r < maze_height
                    and 0 <= next_c and next_c < maze_width
                        and maze[next_r][next_c] == 0):
                    queue.insert(0, (next_r, next_c))
                    # 这些点未来必然要走，做个标记
                    maze[curr[0]][curr[1]] = 2
    return -1


def find_shortest_path(maze_input, start, end):
    maze = copy.deepcopy(maze_input)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    previous_pos = {} # 记录走到本位置前上一次的位置
    queue = []
    queue.insert(0, start)
    maze_height = len(maze)
    maze_width = len(maze[0])
    while queue:
        # print(queue)
        # 走这个点
        curr = queue.pop()
        # 看看是不是终点
        if curr[0] == end[0] and curr[1] == end[1]:
            # 得到路径
            path = [curr]
            while curr in previous_pos:
                curr = previous_pos[curr]
                path.insert(0, curr)
            return path
        for _, dir in enumerate(dirs):
            next_r = curr[0] + dir[0]
            next_c = curr[1] + dir[1]
            if (0 <= next_r and next_r < maze_height
                and 0 <= next_c and next_c < maze_width
                    and maze[next_r][next_c] == 0):
                queue.insert(0, (next_r, next_c))
                # 这些点未来必然要走，做个标记
                maze[curr[0]][curr[1]] = 2
                # 记录一下，从哪里走到（next_c, next_r）这个格子
                previous_pos[(next_r, next_c)] = curr

    return None


import copy

# # 判断从start到end是否有路
# def has_path(maze_input, start ,end):
#     pass

# # 返回从start到end 的最短路径的长度
# def get_shortest_path_length(maze_input, start, end):
#   	pass 


# # 寻找最短路，并以列表形式返回从start到end路上经过的一系列坐标
# def find_shortest_path(maze_input, start, end):
#     pass
    
def see_path(maze,path):     #使寻找到的路径可视化
    for i,p in enumerate(path):
        if i==0:
            maze[p[0]][p[1]] ="S" # start 点
        elif i==len(path)-1:
            maze[p[0]][p[1]]="E" # end 点
        else:
            maze[p[0]][p[1]] =3
    print("\n")
    for r in maze:
        for c in r:
            if c==3:
                print('\033[0;31m'+"*"+" "+'\033[0m',end="")
            elif c=="S" or c=="E":
                print('\033[0;34m'+c+" " + '\033[0m', end="")
            elif c==2:
                print('\033[0;32m'+"#"+" "+'\033[0m',end="")
            elif c==1:
                print('\033[0;;40m'+" "*2+'\033[0m',end="")
            else:
                print(" "*2,end="")
        print()
 



maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
        [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
        [1,1,1,0,0,0,0,0,0,0,0,1,0,1],\
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
start=(1,1)
end=(10,12)
result = has_path(maze, start, end)
print(result) # False


maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
        [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
        [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
start=(1,1)
end=(10,12)
result = get_shortest_path_length2(maze, start, end)
print(result)
result1 = find_shortest_path(maze, start, end) 
print(result1)

see_path(maze, result1)