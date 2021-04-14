#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import maze 
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

#标记 
NOWALL=maze.NOWALL # 无墙
WALL=maze.WALL  # 有墙
WALL2=maze.WALL2  # 有墙

VISIT=maze.VISIT # 到访过
NOVISIT=maze.NOVISIT # 没到过
VERTICAL = maze.VERTICAL # 垂直的
HORIZONTAL = maze.HORIZONTAL# 水平的

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
                opWALL=(r, c, HORIZONTAL)
            if move == 'l':
                newr = r
                newc = c-1
                opWALL=(r, c, VERTICAL)
            if move == 'd':
                newr = r+1
                newc = c
                opWALL=(newr, newc, HORIZONTAL)
            if move == 'r':
                newr = r
                newc = c+1
                opWALL=(newr, newc, VERTICAL)
            # 如果选中的邻居没有被访问:
            if grids[newr][newc] == NOVISIT:
                #   1。移除当前单元格和所选邻居之间的墙。
                #   2。标记被选中的邻居已被拜访过。
                #   3。使选择的邻居成为当前单元格。
                grids[newr][newc]=VISIT
                notusegrids.remove((newr,newc))
                wall[opWALL[0]][opWALL[1]][opWALL[2]] = NOWALL
                r=newr
                c=newc   
            else:
                # 使选择的邻居成为当前单元格。
                r=newr
                c=newc 
    return wall

    
# main
if __name__ == "__main__":
    '''main'''
    aldous_broder_maze(20, 30)
