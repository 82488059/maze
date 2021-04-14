#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import maze
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
#标记 
NOWALL=maze.NOWALL # 无墙
WALL=maze.WALL  # 有墙
WALL2=maze.WALL2  # 有墙

VISIT=maze.VISIT # 到访过
NOVISIT=maze.NOVISIT # 没到过
VERTICAL = maze.VERTICAL # 垂直的
HORIZONTAL = maze.HORIZONTAL# 水平的


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


# main
if __name__ == "__main__":
    '''main'''
    kruskal_maze(20, 30)
