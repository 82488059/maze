#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
import maze 
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
DIAMOND_GREY=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_GREY.fill(COLOR[COLOR_GREY])

# 字体
use_font = pygame.font.Font("FONT.TTF", 16)
# 背景
background=pygame.surface.Surface(size).convert()
background.fill(COLOR[COLOR_BLACK])
# 时间
clock = pygame.time.Clock()

##############################################
#   格子访问标记x,y,0，右墙x,y,1，下墙x,y,2
##############################################


#标记 
NOWALL=maze.NOWALL # 无墙
WALL=maze.WALL  # 有墙
WALL2=maze.WALL2  # 有墙

VISIT=maze.VISIT # 到访过
NOVISIT=maze.NOVISIT # 没到过
VERTICAL = maze.VERTICAL # 垂直的
HORIZONTAL = maze.HORIZONTAL# 水平的

# 随机格子
def wilson_maze_demo(rows, cols):
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols+1)]for i in range(rows+1)]
    # 已访问标记
    grids=[[ NOVISIT for i in range(cols)]for j in range(rows)]
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
    # 标记迷宫
    r,c = random.choice(notusegrids)
    notusegrids.remove((r,c))
    grids[r][c]=VISIT
    # 
    r,c = notusegrids[0]
    tmpgrids.append((r,c))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # 还有格子未访问
        if  notusegrids:
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
                if move == 'u':
                    newr = r-1
                    newc = c
                    nextgrid=(newr, newc)
                    opwall=(r, c, HORIZONTAL)
                if move == 'l':
                    newr = r
                    newc = c-1
                    nextgrid=(newr, newc)
                    opwall=(r, c, VERTICAL)
                if move == 'd':
                    newr = r+1
                    newc = c
                    nextgrid=(newr, newc)
                    opwall=(newr, newc, HORIZONTAL)
                if move == 'r':
                    newr = r
                    newc = c+1
                    nextgrid=(newr, newc)
                    opwall=(newr, newc, VERTICAL)
                # 
                if (newr, newc) in tmpgrids:
                    # 随机到环路
                    i = tmpgrids.index((newr, newc))
                    tmpgrids=tmpgrids[:i+1]
                    tmpwalls=tmpwalls[:i]
                    r=newr
                    c=newc
                elif grids[newr][newc] == VISIT:
                    # 遇到到迷宫
                    tmpwalls.append(opwall)
                    # 加入迷宫
                    for (r,c) in tmpgrids:
                        notusegrids.remove((r,c))
                        grids[r][c]=VISIT
                    for (r,c,x) in tmpwalls:
                        wall[r][c][x]=NOWALL
                        
                    tmpgrids=[]
                    tmpwalls=[]
                    if notusegrids:
                        r,c = notusegrids[0]   
                        tmpgrids.append((r, c))
                else:    
                    tmpgrids.append(nextgrid)
                    tmpwalls.append(opwall)
                    r=newr 
                    c=newc

        screen.blit(background, (0, 0))
        # 格子
        for cx in range(cols):
            for ry in range(rows):
                px,py=1 + (cx) * DIAMOND_SIZE[0], 1 + (ry) * DIAMOND_SIZE[1]
                # 标记访问过的格子
                if NOVISIT == grids[ry][cx]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREY, (px, py))
        # 画格子
        for r1, c1 in tmpgrids:
            px,py=1 + (c1) * DIAMOND_SIZE[0], 1 + (r1) * DIAMOND_SIZE[1]
            screen.blit(DIAMOND_YELLOW, (px, py))

        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*cols+1, 20*rows+1), 2)
        # 画没打通的墙
        for cx in range( cols):
            for ry in range(rows):
                px,py=1 + (cx) * DIAMOND_SIZE[0], 1 + (ry) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_BLACK]
                if WALL == wall[ry][cx][0]:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                if WALL == wall[ry][cx][1]:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)

        # 随机到的墙
        if tmpwalls:
            # 列表中的墙
            for rw,cw,xw in tmpwalls:
                px,py=1 + (cw) * DIAMOND_SIZE[0], 1 + (rw) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_GREEN]
                if xw == VERTICAL:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                else:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)

        # 
        if not notusegrids:
            score_surface = use_font.render("生成完成！", True, COLOR[COLOR_BLACK], COLOR[COLOR_GREY])
            screen.blit(score_surface, (50, rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    wilson_maze_demo(5, 6)
