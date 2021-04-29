#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
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

# pygame
pygame.init()  # 初始化pygame
size = width, height = 800, 600  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
# 颜色
diamond_color_size = 8
COLOR_RED, COLOR_BLUE, COLOR_GREEN, COLOR_YELLOW, COLOR_BLACK, COLOR_GREY, COLOR_GOLDEN, COLOR_NO_DIAMOND = list(range(
    diamond_color_size))
COLOR = {
    COLOR_RED: (255, 0, 0),
    COLOR_BLUE: (0, 0, 255),
    COLOR_GREEN: (0, 255, 0),
    COLOR_YELLOW: (255, 255, 0),
    COLOR_BLACK: (0, 0, 0),
    COLOR_GREY: (250, 240, 230),
    COLOR_GOLDEN : (255,215,0),
    COLOR_NO_DIAMOND: (100, 100, 100),
}
# 格子大小
DIAMOND_SIZE = (20, 20)
# 蓝格子
DIAMOND=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND.fill(COLOR[COLOR_BLUE])
# 绿格子 
DIAMOND_GREEN=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_GREEN.fill(COLOR[COLOR_GREEN])
# 红格子 
DIAMOND_RED=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_RED.fill(COLOR[COLOR_RED])
# 黄格子 
DIAMOND_YELLOW=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_YELLOW.fill(COLOR[COLOR_YELLOW])
# 灰的格子 
DIAMOND_GRAY=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_GRAY.fill(COLOR[COLOR_GREY])
# 
def draw_wall(lw, surface, rgb_color):
    rect = (lw, lw, DIAMOND_SIZE[0] -2*lw, DIAMOND_SIZE[1] -2*lw)
    # 左
    pygame.draw.line(surface, rgb_color, (rect[0], rect[1]), (rect[0], rect[3]), lw)
    # 上
    pygame.draw.line(surface, rgb_color, (rect[0], rect[1]), (rect[2], rect[1]), lw)
    # 下
    pygame.draw.line(surface, rgb_color, (rect[0], rect[3]), (rect[2], rect[3]), lw)
    # 右
    pygame.draw.line(surface, rgb_color, (rect[2], rect[1]), (rect[2], rect[3]), lw)
    return
# 字体
use_font = pygame.font.Font("FONT.TTF", 16)
# 背景
background=pygame.surface.Surface(size).convert()
background.fill(COLOR[COLOR_BLACK])
# 时间
clock = pygame.time.Clock()

#标记 
NOWALL=maze.NOWALL # 无墙
WALL=maze.WALL  # 有墙
WALL2=maze.WALL2  # 有墙

VISIT=maze.VISIT # 到访过
NOVISIT=maze.NOVISIT # 没到过
VERTICAL = maze.VERTICAL # 垂直的
HORIZONTAL = maze.HORIZONTAL# 水平的


# 随机格子
def kruskal_maze(rows, cols):
    # [0]表示格子访问标记
    grids=[[ [0] for i in range(cols)]for i in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
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
            for x in range(0,2):
                # 最左和上的墙不能打通
                if r == 0 and x == 1:
                    continue
                if c == 0 and x == 0:
                    continue
                wallList.append((r,c,x))
    while wallList:
        # 随机选一个墙
        r,c,x = random.choice(wallList)
        # 每个墙随机到一次
        wallList.remove((r,c,x))
        # a,b相邻的集合
        if x == 0: # 竖墙
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
        grids[a[0]][a[1]][0] = 1
        grids[b[0]][b[1]][0] = 1
        # 
        if coll1 != coll2:
            # 打通墙
            wall[r][c][x] = 1
            # 合并集合
            coll = coll1+coll2
            collection.remove(coll1)
            collection.remove(coll2)
            collection.append(coll)
    return wall


# 随机格子
def kruskal_maze_demo(rows, cols):
    # [0]表示格子访问标记
    grids=[[ [0] for i in range(cols)]for i in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
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
            for x in range(0,2):
                # 最左和上的墙不能打通
                if r == 0 and x == 1:
                    continue
                if c == 0 and x == 0:
                    continue
                wallList.append((r,c,x))
    #wall=kruskal_maze(rows, cols)
    #wallList=[]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if  wallList:
            # 随机选一个墙
            r,c,x = random.choice(wallList)
            # 每个墙随机到一次
            wallList.remove((r,c,x))
            # a,b相邻的集合
            if x == 0: # 竖墙
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
            grids[a[0]][a[1]][0] = 1
            grids[b[0]][b[1]][0] = 1
            # 
            if coll1 != coll2:
                # 打通墙
                wall[r][c][x] = 1
                # 合并集合
                coll = coll1+coll2
                collection.remove(coll1)
                collection.remove(coll2)
                collection.append(coll)

        screen.blit(background, (0, 0))
        # 格子
        for cx in range(cols):
            for ry in range(rows):
                px,py=1 + (cx) * DIAMOND_SIZE[0], 1 + (ry) * DIAMOND_SIZE[1]
                # 标记访问过的格子
                if not grids[ry][cx][0]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GRAY, (px, py))

        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*cols+1, 20*rows+1), 2)
        # 画没打通的墙
        for cx in range( cols):
            for ry in range(rows):
                px,py=1 + (cx) * DIAMOND_SIZE[0], 1 + (ry) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_BLACK]
                if not wall[ry][cx][0]:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                if not wall[ry][cx][1]:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)
        
        # 随机到的墙
        if wallList:
            # 列表中的墙
            for rw,cw,xw in wallList:
                px,py=1 + (cw) * DIAMOND_SIZE[0], 1 + (rw) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_GREEN]
                if xw == 0:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                else:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)
            # 当前墙
            px,py=1 + (c) * DIAMOND_SIZE[0], 1 + (r) * DIAMOND_SIZE[1]
            color = COLOR[COLOR_GOLDEN]
            if x == 0:
                pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
            else:
                pygame.draw.line(screen, color, (px, py), (px+20, py), 2)

        # 
        if not wallList:
            score_surface = use_font.render("生成完成！", True, COLOR[COLOR_BLACK], COLOR[COLOR_GREY])
            screen.blit(score_surface, (50, rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    kruskal_maze_demo(20, 30)
