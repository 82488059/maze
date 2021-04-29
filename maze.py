#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random

#标记 
NOWALL=0 # 无墙
WALL=1  # 有墙
WALL2=2  # 有墙

VISIT=1 # 到访过
NOVISIT=0 # 没到过
VERTICAL = 0 # 垂直的
HORIZONTAL = 1# 水平的
INFINITE = -1 # infinite distance 无穷远

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
    grids=[[ NOVISIT for i in range(cols)]for j in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols)]for i in range(rows)]
    notusegrids = [] # 没有访问过的格子
    for tr in range(rows):
        for tc in range(cols):
            notusegrids.append((tr,tc))
    # 选择一个随机的单元格作为当前单元格，并将其标记为已访问的。
    r,c = random.choice(notusegrids)
    # 标记迷宫
    grids[r][c]=VISIT
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
                opwall=(r, c, HORIZONTAL)
            if move == 'l':
                newr = r
                newc = c-1
                opwall=(r, c, VERTICAL)
            if move == 'd':
                newr = r+1
                newc = c
                opwall=(newr, newc, HORIZONTAL)
            if move == 'r':
                newr = r
                newc = c+1
                opwall=(newr, newc, VERTICAL)
            # 如果选中的邻居没有被访问:
            if grids[newr][newc] == NOVISIT:
                #   1。移除当前单元格和所选邻居之间的墙。
                #   2。标记被选中的邻居已被拜访过。
                #   3。使选择的邻居成为当前单元格。
                grids[newr][newc]=VISIT
                notusegrids.remove((newr,newc))
                wall[opwall[0]][opwall[1]][opwall[2]] = NOWALL
                r=newr
                c=newc   
            else:
                # 使选择的邻居成为当前单元格。
                r=newr
                c=newc 
    return wall


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
    history = [(0,0)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][0][1]横墙
    # 左[0]竖墙，上[1]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols)]for i in range(rows)]
    # way用来标记已经访问过的格子
    # 初始化全未访问
    way=[[ NOVISIT for i in range(cols)]for i in range(rows)]
    # 设置起点
    r=0
    c=0
    # 起点加入记录
    history = [(r,c)]
    # 1。选择初始单元格，将其标记为已访问，并将其压入堆栈
    # 2。堆栈不是空的
    while history:
        way[r][c] = VISIT #
        check = []
        # 可以移动到的位置
        if c > 0 and way[r][c-1] == NOVISIT:
            check.append('L')  
        if r > 0 and way[r-1][c] == NOVISIT:
            check.append('U')
        if c < cols-1 and way[r][c+1] == NOVISIT:
            check.append('R')
        if r < rows-1 and way[r+1][c] == NOVISIT:
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
                wall[r][c][0] = NOWALL
                c=c-1
            if move_direction == 'U':
                wall[r][c][1] = NOWALL
                r=r-1
            if move_direction == 'R':
                c=c+1
                wall[r][c][0] = NOWALL
            if move_direction == 'D':
                r=r+1
                wall[r][c][1] = NOWALL
        else: 
            #从堆栈中弹出一个单元格并使其成为当前单元格
            r, c = history.pop()
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

def kruskal_maze(rows, cols):
    # [0]表示格子访问标记
    grids=[[ NOVISIT for i in range(cols)]for i in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols)]for i in range(rows)]
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
            for x in (HORIZONTAL, VERTICAL):
                # 最左和上的墙不能打通
                if r == 0 and x == HORIZONTAL:
                    continue
                if c == 0 and x == VERTICAL:
                    continue
                wallList.append((r,c,x))
    while wallList:
        # 随机选一个墙
        r,c,x = random.choice(wallList)
        # 每个墙随机到一次
        wallList.remove((r,c,x))
        # a,b相邻的集合
        if x == VERTICAL: # 竖墙
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
        grids[a[0]][a[1]] = VISIT
        grids[b[0]][b[1]] = VISIT
        # 
        if coll1 != coll2:
            # 打通墙
            wall[r][c][x] = NOWALL
            # 合并集合
            coll = coll1+coll2
            collection.remove(coll1)
            collection.remove(coll2)
            collection.append(coll)
    return wall


# Randomized Prim's algorithm
#1.Start with a grid full of walls.
#2.Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
#3.While there are walls in the list:
#	1.Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
#		1.Make the wall a passage and mark the unvisited cell as part of the maze.
#		2.Add the neighboring walls of the cell to the wall list.
#	2.Remove the wall from the list.
# 随机普里姆算法
# 1。从布满墙壁的网格开始。
# 2。选一个细胞，把它标记为迷宫的一部分。将单元格的墙添加到墙列表中。
# 3。名单上有墙:
#   1。从列表中随机选择一面墙。如果细胞壁分裂的两个细胞中只有一个被访问，那么:
#       1。将墙壁做成通道，并将未造访的牢房标记为迷宫的一部分。
#       2。将单元格相邻的墙添加到墙列表中。
# 2。把墙从列表中移除。

# 随机墙
# prim算法
def prim_maze(rows, cols):
     # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols+1)]for i in range(rows+1)]
    # 已访问标记
    way=[[ NOVISIT for i in range(cols)]for i in range(rows)]
    # 设置起点
    r=0
    c=0
    # 起点加入记录
    # 标记为迷宫的一部分
    way[r][c]=VISIT
    # 墙列表
    walllist=[]
    walllist.append((r+1,c, HORIZONTAL))
    walllist.append((r,c+1, VERTICAL))
    # 
    while walllist:
        # 随机选一个墙
        r, c, d = random.choice(walllist)
        # 移除墙
        walllist.remove((r,c,d))
        if d == VERTICAL:
            # 如果这面墙分隔的两个单元格只有一个单元格被访问过，那么：
            if c > 0 and (not way[r][c-1] == way[r][c] ):
                #1.把墙打通，将未访问的单元格标记成为迷宫的一部分
                wall[r][c][0]=NOWALL
                if way[r][c] == VISIT:
                    nc=c-1
                else:
                    nc=c
                c=nc
                way[r][c]=VISIT
                #2.将单元格相邻的墙加入到墙列表中
                # 上
                if r > 0 and wall[r][c][1] == WALL:
                    walllist.append((r,c,1))
                # 下
                if r+1 < rows and wall[r+1][c][1] == WALL:
                    walllist.append((r+1,c,1))
                # 左
                if c > 0 and wall[r][c][0] == WALL:
                    walllist.append((r,c,0))
                # 右
                if c+1 < cols and wall[r][c+1][0] == WALL:
                    walllist.append((r,c+1,0))
        elif d == HORIZONTAL:
            # 如果这面墙分隔的两个单元格只有一个单元格被访问过，那么：
            if r > 0 and ( (not way[r-1][c]) == way[r][c] ):
                #1.把墙打通，将未访问的单元格标记成为迷宫的一部分
                wall[r][c][1]=NOWALL
                if way[r][c] == VISIT:
                    nr=r-1
                else:
                    nr=r
                r=nr
                way[r][c]=VISIT
                #2.将单元格相邻的墙加入到墙列表中
                # 上
                if r > 0 and wall[r][c][1] == WALL:
                    walllist.append((r,c,1))
                # 下
                if r + 1 < rows and wall[r+1][c][1] == WALL:
                    walllist.append((r+1,c,1))
                # 左
                if c > 0 and wall[r][c][0] == WALL:
                    walllist.append((r,c,0))
                # 右
                if c + 1 < cols and wall[r][c+1][0] == WALL:
                    walllist.append((r,c+1,0))
        #2.如果墙两面的单元格都已经被访问过，那就从列表里移除这面墙
        for rrr1, ccc1, ddd1 in walllist:
            if ddd1 == VERTICAL:
                if ccc1 > 0 and way[rrr1][ccc1-1] == VISIT and way[rrr1][ccc1] == VISIT:
                    walllist.remove((rrr1,ccc1,ddd1))
            elif ddd1 == HORIZONTAL:
                if rrr1 > 0 and way[rrr1-1][ccc1] == VISIT and way[rrr1][ccc1] == VISIT:
                    walllist.remove((rrr1,ccc1,ddd1))

    return wall




# We begin the algorithm by initializing the maze with one cell chosen arbitrarily.
# Then we start at a new cell chosen arbitrarily,# and perform a random walk until we reach a cell already in the maze—however, 
# if at any point the random walk reaches its own path, forming a loop,
# we erase the loop from the path before proceeding.
# When the path reaches the maze, we add it to the maze. 
# Then we perform another loop-erased random walk from another arbitrary starting cell, 
# repeating until all cells have been filled.

# This procedure remains unbiased no matter which method we use to arbitrarily choose starting cells.
#  So we could always choose the first unfilled cell in (say) left-to-right, top-to-bottom order for simplicity.

# 我们任意选择一个单元格开始初始化迷宫算法。
# 然后我们随机选择一个新单元格，开始执行随机漫步，直到我们到达迷宫中已经存在的单元格，然而，
# 如果在任意一点随机漫步到达自己的路径，形成一个循环，在继续之前从路径中删除循环。
# 当路径到达迷宫时，我们将其添加到迷宫中。
# 然后我们从另一个任意的起始单元执行另一个循环擦除的随机漫步，
# 重复，直到填充完所有单元格。

# 无论我们使用哪种方法来选择开始单元格，这个过程都是无偏的。
# 因此，为了简单起见，我们可以按照从左到右、从上到下的顺序选择第一个未填充的单元格。
def wilson_maze(rows, cols):
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols+1)]for i in range(rows+1)]
    # 已访问标记
    grids=[[ NOVISIT for i in range(cols)]for j in range(rows)]
    # 我们任意选择一个单元格开始初始化迷宫算法。
    # 然后我们随机选择一个新单元格，开始执行随机漫步，直到我们到达迷宫中已经存在的单元格，然而，
    # 如果在任意一点随机漫步到达自己的路径，形成一个循环，在继续之前从路径中删除循环。
    # 当路径到达迷宫时，我们将其添加到迷宫中。
    # 然后我们从另一个任意的起始单元执行另一个循环擦除的随机漫步，
    # 重复，直到填充完所有单元格。

    # 无论我们使用哪种方法来选择开始单元格，这个过程都是无偏的。
    # 因此，为了简单起见，我们可以按照从左到右、从上到下的顺序选择第一个未填充的单元格。
    tmpgrids = [] # 临时路径
    tmpwalls = [] # 临时路径中的墙
    notusegrids = [] # 没有访问过的格子
    for tr in range(rows):
        for tc in range(cols):
            notusegrids.append((tr,tc))
    r,c = random.choice(notusegrids)
    notusegrids.remove((r,c))
    # 标记迷宫
    grids[r][c]=VISIT
    # 
    r,c = notusegrids[0]
    tmpgrids.append((r,c))

    while  notusegrids:
        #r,c = notusegrids[0]
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
                nextgrid=(newr, newc)
                opwall=(r, c, HORIZONTAL)
            if move == 'l':
                newr = r
                newc = c-1
                nextgrid=(newr, newc)
                opwall=(r, c, VERTICAL)
            if move == 'd':
                newr = r+1
                newc = c
                nextgrid=(newr, newc)
                opwall=(newr, newc, HORIZONTAL)
            if move == 'r':
                newr = r
                newc = c+1
                nextgrid=(newr, newc)
                opwall=(newr, newc, VERTICAL)
            # 
            if (newr, newc) in tmpgrids:
                # 随机到环路
                i = tmpgrids.index((newr, newc))
                tmpgrids=tmpgrids[:i+1]
                tmpwalls=tmpwalls[:i]
                r=newr
                c=newc
            elif grids[newr][newc] == VISIT:
                # 遇到到迷宫
                tmpwalls.append(opwall)
                # 加入迷宫
                for (r,c) in tmpgrids:
                    notusegrids.remove((r,c))
                    grids[r][c]=VISIT
                for (r,c,x) in tmpwalls:
                    wall[r][c][x]=NOWALL
                    
                tmpgrids=[]
                tmpwalls=[]
                if notusegrids:
                    r,c = notusegrids[0]   
                    tmpgrids.append((r, c))
            else:    
                tmpgrids.append(nextgrid)
                tmpwalls.append(opwall)
                r=newr 
                c=newc

    return wall

# 拆出第二条路
# 下一圈
def FindNextCircle(startList, walls, grids, rows, cols):
    startNextList = [] # 下一步
    for node in startList:
        r, c = node
        l = grids[r][c]
        # 可以到达的位置
        if r>0 and NOWALL == walls[r][c][1] and INFINITE == grids[r-1][c]:
            # move = 'u'
            nr=r-1
            nc=c
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
        if c>0 and NOWALL == walls[r][c][0] and INFINITE == grids[r][c-1]:
            # move = 'l'
            nr=r
            nc=c-1
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
        if c<cols-1 and NOWALL == walls[r][c+1][0] and INFINITE == grids[r][c+1] :
            # move='r'
            nr=r
            nc=c+1
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
        if r<rows-1 and NOWALL == walls[r+1][c][1] and INFINITE == grids[r+1][c] :
            # move='d'
            nr=r+1
            nc=c
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
    # 下一圈
    startList.clear()
    startList.extend(startNextList)
    return startList

# 拆出第二条路
# 拆分迷宫
def split_maze(walls, grids, startPoint, endPoint, startMap, endMap, rows, cols):
    startList = [startPoint]
    endList = [endPoint]
    startMap.append(startPoint)
    endMap.append(endPoint)
    while startList or endList:
        split_maze_step(walls, grids, startList, endList, startMap, endMap, rows, cols)
    return startMap, endMap

# 拆出第二条路
# 一步一步执行
def split_maze_step(walls, grids, startList, endList, startMap, endMap, rows, cols):
    # 起点
    FindNextCircle(startList, walls, grids, rows, cols)
    startMap+=startList
    # 终点
    FindNextCircle(endList, walls, grids, rows, cols)
    endMap+=endList
    return startList, endList

# 找到分隔两部分的墙
def find_partition_walls(walls, startMap, endMap, rows, cols):
    tmp_grids=[[ 'e' for i in range(cols)]for j in range(rows)]
    for s in startMap:
        tmp_grids[s[0]][s[1]] = 's'
    part = []
    for r in range(rows):
        for c in range(cols):
            if WALL == walls[r][c][0] and c > 0:
                if tmp_grids[r][c-1] != tmp_grids[r][c]:
                    part.append((r,c,0))
            if WALL == walls[r][c][1] and r > 0:
                if tmp_grids[r-1][c] != tmp_grids[r][c]:
                    part.append((r,c,1))
    return part


# 拆出第二条路
def down_wall_maze(walls, rows, cols, startPoint, endPoint):
    startList=[startPoint]
    endList=[endPoint]
    ## 
    grids=[[ INFINITE for i in range(cols)]for j in range(rows)]
    grids[startPoint[0]][startPoint[1]]=0 # 标记已经到过格子距离
    grids[endPoint[0]][endPoint[1]]=0
    # 
    startMap=[]
    endMap=[]
    startMap += startList
    endMap += endList
    # 
    split_maze(walls, grids, startPoint, endPoint, startMap, endMap, rows, cols)
    # 
    parts = find_partition_walls(walls, startMap, endMap, rows, cols)
    down_wall = random.choice(parts)
    swr, swc, swd = down_wall
    parts.remove((swr, swc, swd))
    walls[swr][swc][swd] = NOWALL
    return walls


# main
if __name__ == "__main__":
    '''main'''
    aldous_broder_maze(20, 30)


