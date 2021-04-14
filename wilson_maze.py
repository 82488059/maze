#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
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

##############################################
#   格子访问标记x,y,0，右墙x,y,1，下墙x,y,2
##############################################

# 
def add2maze(grids, notusegrids, tgrids, twalls):
    for (r,c) in tgrids:
        notusegrids.remove((r,c))
        grids[r][c][0]=1
    for (r,c,x) in twalls:
        grids[r][c][x]=1 
    return 

# 随机格子
def wilson_maze(rows, cols):
    # 墙 [0]表示格子访问标记，右[1]竖墙，下[2]横墙
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。下墙同理)
    # 初始化未访问，墙未打通
    grids=[[ [0,0,0] for i in range(cols)]for j in range(rows)]
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
    # 标记为迷宫
    grids[r][c][0]=1
    # 开始随机的单元格
    r,c = notusegrids[0]
    tmpgrids.append((r,c))
    # 还有格子未访问
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
            # 计算下一个格子坐标和需要拆开的墙的坐标
            if move == 'u':
                newr = r-1
                newc = c
                nextgrid=(newr, newc)
                opwall=(newr, newc, 2)
            if move == 'l':
                newr = r
                newc = c-1
                nextgrid=(newr, newc)
                opwall=(newr, newc, 1)
            if move == 'd':
                newr = r+1
                newc = c
                nextgrid=(newr, newc)
                opwall=(r, c, 2)
            if move == 'r':
                newr = r
                newc = c+1
                nextgrid=(newr, newc)
                opwall=(r, c, 1)
            # 判断
            if (newr, newc) in tmpgrids:
                # 随机到环路
                i = tmpgrids.index((newr, newc))
                tmpgrids=tmpgrids[:i+1]
                tmpwalls=tmpwalls[:i]
                r=newr
                c=newc
            elif grids[newr][newc][0] == 1:
                # 遇到到迷宫
                tmpwalls.append(opwall)
                # 路径添加到迷宫
                add2maze(grids, notusegrids, tmpgrids, tmpwalls)      
                tmpgrids=[]
                tmpwalls=[]
                # 还有格子未加入迷宫，继续随机
                if notusegrids:
                    r,c = notusegrids[0]   
                    tmpgrids.append((r, c))
            else:    
                # 其它情况继续随机
                tmpgrids.append(nextgrid)
                tmpwalls.append(opwall)
                r=newr 
                c=newc

    return grids



# main
if __name__ == "__main__":
    '''main'''
    wilson_maze(20, 30)
