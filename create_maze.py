#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random


# 算法
def depth_maze(rows, cols):
    num_cols=cols
    num_rows=rows
    history = [(0,0)]
    # 墙 0墙 [0]竖墙[1]横墙
    wall=[[ [0,0] for i in range(num_cols)]for i in range(num_rows)]
    # 走过的标记
    way=[[ 0 for i in range(num_cols)]for i in range(num_rows)]
    r=0
    c=0
    # 出发点
    history = [(r,c)]
    # 1.将起点作为当前迷宫单元并标记为已访问
    # 2.当还存在未标记的迷宫单元，进行循环
    while history:
        way[r][c] = 1 #
        check = []
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
            move_direction = random.choice(check)
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


