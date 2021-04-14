
#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random

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
#标记 
WALL=1  # 有墙
NOWALL=0 # 无墙
VISIT=1 # 到访过
NOVISIT=0 # 没到过
VERTICAL = 0 # 垂直的
HORIZONTAL = 1# 水平的

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
        rr,cc,dd=r,c,d
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

