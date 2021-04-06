
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

# 随机墙
# prim算法
def prim_maze(rows, cols):
    num_cols=cols
    num_rows=rows
    # 墙 0表示通路 |竖墙 -横墙
    wall=[[ ['|','-'] for i in range(num_cols+1)]for i in range(num_rows+1)]
    # 已访问标记
    way=[[ 0 for i in range(num_cols)]for i in range(num_rows)]
    # 设置起点
    r=0
    c=0
    # 起点加入记录
    # 标记为迷宫的一部分
    way[r][c]=1
    # 墙列表
    walllist=[]
    walllist.append((r+1,c,'-'))
    walllist.append((r,c+1,'|'))
    # 
    while walllist:
        # 随机选一个墙
        r, c, d = random.choice(walllist)
        # 移除墙
        walllist.remove((r,c,d))
        if d == '|':
            # 如果这面墙分隔的两个单元格只有一个单元格被访问过，那么：
            if c > 0 and (not way[r][c-1] == way[r][c] ):
                #1.把墙打通，将未访问的单元格标记成为迷宫的一部分
                wall[r][c][0]=0
                if way[r][c] == 1:
                    nc=c-1
                else:
                    nc=c
                c=nc
                way[r][c]=1
                #2.将单元格相邻的墙加入到墙列表中
                # 上
                if r > 0 and wall[r][c][1] == '-':
                    walllist.append((r,c,'-'))
                # 下
                if r+1 < num_rows and wall[r+1][c][1] == '-':
                    walllist.append((r+1,c,'-'))
                # 左
                if c > 0 and wall[r][c][0] == '|':
                    walllist.append((r,c,'|'))
                # 右
                if c+1 < num_cols and wall[r][c+1][0] == '|':
                    walllist.append((r,c+1,'|'))
        elif d == '-':
            # 如果这面墙分隔的两个单元格只有一个单元格被访问过，那么：
            if r > 0 and ( (not way[r-1][c]) == way[r][c] ):
                #1.把墙打通，将未访问的单元格标记成为迷宫的一部分
                wall[r][c][1]=0
                if way[r][c] == 1:
                    nr=r-1
                else:
                    nr=r
                r=nr
                way[r][c]=1
                #2.将单元格相邻的墙加入到墙列表中
                # 上
                if r > 0 and wall[r][c][1] == '-':
                    walllist.append((r,c,'-'))
                # 下
                if r + 1 < num_rows and wall[r+1][c][1] == '-':
                    walllist.append((r+1,c,'-'))
                # 左
                if c > 0 and wall[r][c][0] == '|':
                    walllist.append((r,c,'|'))
                # 右
                if c + 1 < num_cols and wall[r][c+1][0] == '|':
                    walllist.append((r,c+1,'|'))
        #2.如果墙两面的单元格都已经被访问过，那就从列表里移除这面墙
        for rrr1, ccc1, ddd1 in walllist:
            if ddd1 == '|':
                if ccc1 > 0 and way[rrr1][ccc1-1] == 1 and way[rrr1][ccc1] == 1:
                    walllist.remove((rrr1,ccc1,ddd1))
            elif ddd1 == '-':
                if rrr1 > 0 and way[rrr1-1][ccc1] == 1 and way[rrr1][ccc1] == 1:
                    walllist.remove((rrr1,ccc1,ddd1))
    return wall

