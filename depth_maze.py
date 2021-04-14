#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
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
WALL=0  # 有墙
NOWALL=1 # 无墙
VISIT=1 # 到访过
NOVISIT=0 # 没到过
VERTICAL = 0 # 垂直的
HORIZONTAL = 1# 水平的


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

