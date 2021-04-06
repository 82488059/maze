#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
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

# 随机格子
def kruskal_maze(rows, cols):
    # 墙 [0]表示格子访问标记，右[1]竖墙，下[2]横墙
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。下墙同理)
    # 初始化未访问，墙未打通
    grids=[[ [0,0,0] for i in range(cols)]for i in range(rows)]
    # 设置起点
    r=0
    c=0
    # 格子列表
    gridlist=[]
    gridlist.append((r,c))
    # 单元格集合
    collection =[]
    # 墙壁的列表
    walls=[]
    for r in range(rows):
        for c in range(cols):
            collection.append([(r,c)])
            for x in range(1,3):
                # 最右和最下的墙不能打通
                if r == rows - 1 and x == 2:
                    continue
                if c == cols - 1 and x == 1:
                    continue
                walls.append((r,c,x))

    while walls:
        # 随机选一个墙
            r,c,x = random.choice(walls)
            # a,b相邻的集合
            if x == 1: # 竖墙
                a = (r,c)
                b = (r,c+1)
            else :  # 横墙
                a = (r,c)
                b = (r+1,c)
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
            if coll1 == coll2:
                walls.remove((r,c,x))
            else:
                # 打通墙
                grids[r][c][x] = 1
                # 
                coll = coll1+coll2
                collection.remove(coll1)
                collection.remove(coll2)
                collection.append(coll)
                walls.remove((r,c,x))
        
    return grids



# main
if __name__ == "__main__":
    '''main'''
    kruskal_maze(20, 30)
