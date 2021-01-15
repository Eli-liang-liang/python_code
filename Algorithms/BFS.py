# example 1
# maze : List[List[int]]
maze = [ [0,0,1,0,0],
         [0,0,0,0,0],
         [0,0,0,1,0],
         [1,1,0,1,1],
         [0,0,0,0,0] ]
# start : List[int]
start = [0,4]
# destination : List[int]
destination = [4,4]
# return -> bool
def hasPath(maze, start, destination):
    q = []
    q.append(start)
    maze_width = len(maze(0))
    maze_height = len(maze)

    visited =[ [ 0 for _ in range(maze_width) ] for _ in range(maze_height) ]
    while(q):
        temp_xy = q.pop(0)
        x = temp_xy[0]
        y = temp_xy[1]
        visited[x][y] = 1
        if x == destination[0] and y == destination[1]:
            return True
# right
        next_x = x
        next_y = y
        for next_x in range(x, maze_width):
            if (maze[next_x][next_y] == 0):
                continue
        if visited[next_x,next_y] == 0:
            q.append([next_x, next_y])

        next_x = x
        next_y = y
        for next_x in range(x, 0):
            if (maze[next_x][next_y] == 0):
                continue
       if visited[next_x,next_y] == 0:
            q.append([next_x, next_y])


        next_x = x
        next_y = y
        for next_y in range(y, 0, -1):
            if (maze[next_x][next_y] == 0):
                continue
       if visited[next_x,next_y] == 0:
            q.append([next_x, next_y])


        next_x = x
        next_y = y
        for next_y in range(y, maze_height):
            if (maze[next_x][next_y] == 0):
                continue
       if visited[next_x,next_y] == 0:
            q.append([next_x, next_y])
    
    return False
