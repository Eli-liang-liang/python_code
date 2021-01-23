# dirs=[(0,1),(1,0),(0,-1),(-1,0)] #当前位置四个方向的偏移量
# path=[]              #存找到的路径
 
# def mark(maze,pos):  #给迷宫maze的位置pos标"2"表示“倒过了”
#     maze[pos[0]][pos[1]]=2
 
# def passable(maze,pos): #检查迷宫maze的位置pos是否可通行
#     return maze[pos[0]][pos[1]]==0
 
# def find_path(maze,pos,end):
#     mark(maze,pos)
#     if pos==end:
#         print(pos,end=" ")  #已到达出口，输出这个位置。成功结束
#         path.append(pos)
#         return True
#     for i in range(4):      #否则按四个方向顺序检查
#         nextp=pos[0]+dirs[i][0],pos[1]+dirs[i][1]
#         #考虑下一个可能方向
#         if passable(maze,nextp):        #不可行的相邻位置不管
#             if find_path(maze,nextp,end):#如果从nextp可达出口，输出这个位置，成功结束
#                 print(pos,end=" ")
#                 path.append(pos)
#                 return True
#     return False
 
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
 
# if __name__ == '__main__':
#     maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
#           [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
#           [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
#           [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
#           [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
#           [1,0,1,1,1,1,1,1,1,1,0,0,0,1],\
#           [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
#           [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
#           [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
#           [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
#           [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
#           [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
#     start=(1,1)
#     end=(10,12)
#     find_path(maze,start,end)
#     see_path(maze, path)

import copy

def has_path(maze_input, start, end):
    maze = copy.deepcopy(maze_input)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    maze_height = len(maze)
    maze_width = len(maze[0])
 
    def dfs(maze, start, end):
        curr = start
        maze[curr[0]][curr[1]] = 2
        if (start[0] == end[0] and start[1] == end[1]):
            return True

        for _, dir in enumerate(dirs):
            next_r = curr[0] + dir[0]
            next_c = curr[1] + dir[1]
            if (0 <= next_r and next_r < maze_height
                and 0 <= next_c and next_c < maze_width
                    and maze[next_r][next_c] == 0):
                if (dfs(maze, [next_r, next_c], end)): # 能找到的话
                    return True
        return False
 
    return dfs(maze, start, end)

def find_one_path(maze_input, start, end):
    maze = copy.deepcopy(maze_input)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    path = []
    maze_height = len(maze) 
    maze_width = len(maze[0])
 
    def dfs(maze, start, end):
        curr = start
        path.append(curr)
        see_path(maze, path)
        maze[curr[0]][curr[1]] = 2
        if (start[0] == end[0] and start[1] == end[1]):
            return True

        for _, dir in enumerate(dirs):
            next_r = curr[0] + dir[0]
            next_c = curr[1] + dir[1]
            next_path = path[:]
            next_path.append([next_r, next_c])
            see_path(maze, next_path)
            if (0 <= next_r and next_r < maze_height
                and 0 <= next_c and next_c < maze_width
                    and maze[next_r][next_c] == 0):
                if (dfs(maze, [next_r, next_c], end)): # 能找到的话
                    return True
        
        path.pop()
        return False
 
    result = dfs(maze, start, end)

    if result == True:
        return path
    else:
        return None
    return None



def find_all_paths(maze_input, start, end):
    maze = copy.deepcopy(maze_input)
    dirs = [[0,1],[1,0],[0,-1],[-1,0]] #当前位置四个方向的偏移量
    paths = []
    path = []
    maze_height = len(maze)
    maze_width = len(maze[0])
 
    def dfs(maze, start, end):
        path.append(start)
        see_path(maze, path)
        curr = start
        maze[curr[0]][curr[1]] = 2
        if (start[0] == end[0] and start[1] == end[1]):
            paths.append(path[:])
            maze[curr[0]][curr[1]] = 0
            path.pop()
            return True
        for _, dir in enumerate(dirs):
            next_r = curr[0] + dir[0]
            next_c = curr[1] + dir[1]
            next_path = path[:]
            next_path.append([next_r, next_c])
            see_path(maze, next_path)
            if (0 <= next_r and next_r < maze_height
                and 0 <= next_c and next_c < maze_width
                    and maze[next_r][next_c] == 0):
                dfs(maze, [next_r, next_c], end)
        
        maze[curr[0]][curr[1]] = 0
        path.pop()
        return False
 
    dfs(maze, start, end)
    return paths




 
def see_path(maze_input,path):     #使寻找到的路径可视化
    maze = copy.deepcopy(maze_input)
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
# result = has_path(maze, start, end)
# print(result) # True

# path = find_one_path(maze,start,end)
# print(path)
# see_path(maze, path)

# paths = find_all_paths(maze,start,end)
# for path in paths:
#     see_path(maze, path)


maze=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1],\
        [1,0,0,0,1,1,0,0,0,1,0,0,0,1],\
        [1,0,1,0,0,0,0,1,0,1,0,1,0,1],\
        [1,0,1,0,1,1,1,1,0,1,0,1,0,1],\
        [1,0,1,0,0,0,0,0,0,1,1,1,0,1],\
        [1,0,1,1,1,0,1,1,1,1,0,0,0,1],\
        [1,0,1,0,0,0,0,0,0,0,0,1,0,1],\
        [1,0,0,0,1,1,1,0,1,0,1,1,0,1],\
        [1,0,1,0,1,0,1,0,1,0,1,0,0,1],\
        [1,0,1,0,1,0,1,0,1,1,1,1,0,1],\
        [1,0,1,0,0,0,1,0,0,1,0,0,0,1],\
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
start=(1,1)
end=(10,12)
result = has_path(maze, start, end)
print(result) # True

path = find_one_path(maze,start,end)
print(path)
see_path(maze, path)

paths = find_all_paths(maze,start,end)
for path in paths:
    print(path)
    see_path(maze, path)