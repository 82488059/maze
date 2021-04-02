#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random

# 墙不占用单元格
# 可以保证所有的格都是相通的
# 深度优先算法可以遍历所有的单元格。

# Recursive backtracker
# 递归回溯算法
def depth_maze(rows, cols):
    num_cols=cols
    num_rows=rows
    history = [(0,0)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][0][1]横墙
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
    # 1.将起点作为当前迷宫单元并标记为已访问
    # 2.当还存在未标记的迷宫单元，进行循环
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
        # 2.1.如果当前迷宫单元有未被访问过的的相邻的迷宫单元
        # 2.1.1.随机选择一个未访问的相邻迷宫单元
		# 2.1.2.将当前迷宫单元入栈
        # 2.1.3.移除当前迷宫单元与相邻迷宫单元的墙
		# 2.1.4.标记相邻迷宫单元并用它作为当前迷宫单元
        if len(check): 
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
            #2.2.如果当前迷宫单元不存在未访问的相邻迷宫单元，并且栈不空
		    #2.2.1.栈顶的迷宫单元出栈
		    #2.2.2.令其成为当前迷宫单元
            r, c = history.pop()
    return wall

