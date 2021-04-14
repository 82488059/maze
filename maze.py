#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random

#标记 
WALL=0  # 有墙
NOWALL=1 # 无墙
VISIT=1 # 到访过
NOVISIT=0 # 没到过
VERTICAL = 0 # 垂直的
HORIZONTAL = 1# 水平的


# Randomized depth-first search
# Recursive implementation
#1。Choose the initial cell, mark it as visited and push it to the stack
#2。While the stack is not empty
#   1。Pop a cell from the stack and make it a current cell
#   2。If the current cell has any neighbours which have not been visited
#       1。Push the current cell to the stack
#       2。Choose one of the unvisited neighbours
#       3。Remove the wall between the current cell and the chosen cell
#       4。Mark the chosen cell as visited and push it to the stack
#随机深度优先搜索
#递归实现
#1。选择初始单元格，将其标记为已访问，并将其压入堆栈
#2。而堆栈不是空的
#   1。从堆栈中弹出一个单元格并使其成为当前单元格
#   2。如果当前单元有任何未被访问的邻居
#       1。将当前单元格压入堆栈
#       2。选择一个未被拜访的邻居
#       3。移除当前单元格和所选单元格之间的墙
#       4。将选中的单元格标记为已访问的，并将其压入堆栈
# 墙不占用单元格
# 可以保证所有的格都是相通的
# 深度优先算法可以遍历所有的单元格。
# Randomized depth-first search
# Recursive backtracker
# 递归回溯算法
def depth_maze(rows, cols):
    num_cols=cols
    num_rows=rows
    history = [(0,0)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][0][1]横墙
    # 左[0]竖墙，上[1]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(num_cols)]for i in range(num_rows)]
    # way用来标记已经访问过的格子
    # 初始化全未访问
    way=[[ 0 for i in range(num_cols)]for i in range(num_rows)]
    # 设置起点
    r=0
    c=0
    # 起点加入记录
    history = [(r,c)]
    # 1。选择初始单元格，将其标记为已访问，并将其压入堆栈
    # 2。堆栈不是空的
    while history:
        way[r][c] = 1 #
        check = []
        # 可以移动到的位置
        if c > 0 and way[r][c-1] == 0:
            check.append('L')  
        if r > 0 and way[r-1][c] == 0:
            check.append('U')
        if c < num_cols-1 and way[r][c+1] == 0:
            check.append('R')
        if r < num_rows-1 and way[r+1][c] == 0:
            check.append('D')    
        # 如果当前单元有任何未被访问的邻居
        if len(check): 
            # 选择一个未被拜访的邻居
            # 移除当前单元格和所选单元格之间的墙
            # 将选中的单元格标记为已访问的，并将其压入堆栈
            history.append((r, c))
            # 随机移动
            move_direction = random.choice(check)
            # 打通墙壁
            if move_direction == 'L':
                wall[r][c][0] = 1
                c=c-1
            if move_direction == 'U':
                wall[r][c][1] = 1
                r=r-1
            if move_direction == 'R':
                c=c+1
                wall[r][c][0] = 1
            if move_direction == 'D':
                r=r+1
                wall[r][c][1] = 1
        else: 
            #从堆栈中弹出一个单元格并使其成为当前单元格
            r, c = history.pop()
    return wall



#Aldous-Broder algorithm
#The Aldous-Broder algorithm also produces uniform spanning trees.

# 1.Pick a random cell as the current cell and mark it as visited.
# 2.While there are unvisited cells:
#   1.Pick a random neighbour.
#   2.If the chosen neighbour has not been visited:
#       1.Remove the wall between the current cell and the chosen neighbour.
#       2.Mark the chosen neighbour as visited.
#   3.Make the chosen neighbour the current cell.

# Aldous-Broder算法
# Aldous-Broder算法也生成统一的生成树。
# 1。选择一个随机的单元格作为当前单元格，并将其标记为已访问的。
# 2。当存在未访问细胞时:
#   1。随机选择一个邻居。
#   2。如果选中的邻居没有被访问:
#       1。移除当前单元格和所选邻居之间的墙。
#       2。标记被选中的邻居已被拜访过。
#   3。使选择的邻居成为当前单元格。

def aldous_broder_maze(rows, cols):
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化未访问，墙未打通
    grids=[[ [0] for i in range(cols)]for j in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
    notusegrids = [] # 没有访问过的格子
    for tr in range(rows):
        for tc in range(cols):
            notusegrids.append((tr,tc))
    # 选择一个随机的单元格作为当前单元格，并将其标记为已访问的。
    r,c = random.choice(notusegrids)
    # 标记迷宫
    grids[r][c][0]=1
    notusegrids.remove((r,c))
    # 当存在未访问细胞时:
    while notusegrids:
        directions = []
        # 可随机方向
        if r > 0:
            directions.append('u')
        if c > 0:
            directions.append('l')
        if r < rows-1:
            directions.append('d')
        if c < cols-1:
            directions.append('r')
        if len(directions):
            # 随机一个方向
            move = random.choice(directions)
            if move == 'u':
                newr = r-1
                newc = c
                opwall=(r, c, 1)
            if move == 'l':
                newr = r
                newc = c-1
                opwall=(r, c, 0)
            if move == 'd':
                newr = r+1
                newc = c
                opwall=(newr, newc, 1)
            if move == 'r':
                newr = r
                newc = c+1
                opwall=(newr, newc, 0)
            # 如果选中的邻居没有被访问:
            if grids[newr][newc][0] == 0:
                #   1。移除当前单元格和所选邻居之间的墙。
                #   2。标记被选中的邻居已被拜访过。
                #   3。使选择的邻居成为当前单元格。
                grids[newr][newc][0]=1
                notusegrids.remove((newr,newc))
                wall[opwall[0]][opwall[1]][opwall[2]] = 1
                r=newr
                c=newc   
            else:
                # 使选择的邻居成为当前单元格。
                r=newr
                c=newc 
    return wall


# Randomized Kruskal's algorithm
# This algorithm is a randomized version of Kruskal's algorithm.
# 1.Create a list of all walls, and create a set for each cell, each containing just that one cell.
# 2.For each wall, in some random order:
#    1.If the cells divided by this wall belong to distinct sets:
#        1.Remove the current wall.
#        2.Join the sets of the formerly divided cells.
# 随机的Kruskal算法
# 这个算法是Kruskal算法的随机化版本。
# 1。创建所有墙壁的列表，并为每个单元格创建一个集合，每个单元格只包含一个单元格。
# 2。对于每一面墙，以一些随机的顺序:
#   1。如果由这个壁分隔的细胞属于不同的集合:
#       1。移除当前的墙。
#       2。加入以前分裂的细胞组。

##############################################
#   格子访问标记x,y,0，x,y右墙x,y,1，下墙x,y,2。
##############################################
def kruskal_maze(rows, cols):
    # [0]表示格子访问标记
    grids=[[ [0] for i in range(cols)]for i in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
    # 设置起点
    r=0
    c=0
    # 格子列表
    gridlist=[]
    gridlist.append((r,c))
    # 单元格集合
    collection =[]
    # 墙壁的列表
    wallList=[]
    for r in range(rows):
        for c in range(cols):
            collection.append([(r,c)])
            for x in range(0,2):
                # 最左和上的墙不能打通
                if r == 0 and x == 1:
                    continue
                if c == 0 and x == 0:
                    continue
                wallList.append((r,c,x))
    while wallList:
        # 随机选一个墙
        r,c,x = random.choice(wallList)
        # 每个墙随机到一次
        wallList.remove((r,c,x))
        # a,b相邻的集合
        if x == 0: # 竖墙
            a = (r,c-1)
            b = (r,c)
        else :  # 横墙
            a = (r,c)
            b = (r-1,c)
        coll1 = []
        coll2 = []
        for coll in collection:
            if a in coll:
                coll1 = coll
            if b in coll:
                coll2 = coll
        # 设置访问过
        grids[a[0]][a[1]][0] = 1
        grids[b[0]][b[1]][0] = 1
        # 
        if coll1 != coll2:
            # 打通墙
            wall[r][c][x] = 1
            # 合并集合
            coll = coll1+coll2
            collection.remove(coll1)
            collection.remove(coll2)
            collection.append(coll)
    return wall
    
# main
if __name__ == "__main__":
    '''main'''
    aldous_broder_maze(20, 30)
