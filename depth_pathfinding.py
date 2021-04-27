#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
#import depth_maze
import maze
#import aldous_broder_maze

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
# 文字
score_surface = use_font.render("找到终点", True, COLOR[COLOR_BLACK], COLOR[COLOR_GREY])
            
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
INFINITE = maze.INFINITE # 无穷远

# 

# 深度优先寻路演示代码
def depth_pathfinding(rows, cols, walls, startPoint=(0,0), endPoint=None):
    # walls = depth_maze.depth_maze(rows, cols)
    grids=[[ maze.NOVISIT for i in range(cols)]for j in range(rows)]
    # 标记迷宫
    findEndPoint=False
    # 起点
    r = startPoint[0]
    c = startPoint[1]
    # 终点
    if endPoint:
        stopPoint=endPoint
    else:
        stopPoint=(rows-1,cols-1)

    pathList=[(r,c)] # 路径
    grids[r][c]=maze.VISIT # 标记已经到过格子
    # 当存在未访问格子时:
    while pathList and not findEndPoint:        
        move=None
        if r>0 and maze.NOWALL == walls[r][c][1] and maze.VISIT != grids[r-1][c]:
            move = 'u'
            nr=r-1
            nc=c
        elif c>0 and maze.NOWALL == walls[r][c][0] and maze.VISIT != grids[r][c-1]:
            move='l'
            nr=r
            nc=c-1
        elif c<cols-1 and maze.NOWALL == walls[r][c+1][0] and maze.VISIT != grids[r][c+1] :
            move='r'
            nr=r
            nc=c+1
        elif r<rows-1 and maze.NOWALL == walls[r+1][c][1] and maze.VISIT != grids[r+1][c] :
            move='d'
            nr=r+1
            nc=c
        if move:
            # 加入路径
            pathList.append((r,c))
            # move到下个点
            r=nr
            c=nc
            if (r,c) == stopPoint:
                # 终点加入路径
                pathList.append((r,c))
                findEndPoint=True
            else:
                grids[r][c]=maze.VISIT
        else:
            (r,c) = pathList.pop()

    return pathList


# 深度优先寻路演示代码
def depth_pathfinding_demo(rows, cols):
    #walls = maze.aldous_broder_maze(rows, cols)
    walls = maze.depth_maze(rows, cols)
    #walls = maze.kruskal_maze(rows, cols)
    #walls = maze.prim_maze(rows, cols)
    #walls = maze.wilson_maze(rows, cols)
    # fpath = depth_pathfinding(rows,cols, walls)
    POSX=40
    POSY=40
    # 初始化未访问，墙未打通
    grids=[[ maze.NOVISIT for i in range(cols)]for j in range(rows)]
    # 标记迷宫
    r=0
    c=0
    findEndPoint=False
    # 起点
    startPoint=(r,c)
    # 终点
    stopPoint=(rows-1,cols-1)
    pathList=[(r,c)] # 路径
    grids[r][c]=maze.VISIT # 标记已经到过格子
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # 当存在未访问细胞时:
        if  pathList and not findEndPoint:        
            move=None
            if r>0 and maze.NOWALL == walls[r][c][1] and maze.VISIT != grids[r-1][c]:
                move = 'u'
                nr=r-1
                nc=c
            elif c>0 and maze.NOWALL == walls[r][c][0] and maze.VISIT != grids[r][c-1]:
                move='l'
                nr=r
                nc=c-1
            elif c<cols-1 and maze.NOWALL == walls[r][c+1][0] and maze.VISIT != grids[r][c+1] :
                move='r'
                nr=r
                nc=c+1
            elif r<rows-1 and maze.NOWALL == walls[r+1][c][1] and maze.VISIT != grids[r+1][c] :
                move='d'
                nr=r+1
                nc=c
            if move:
                # 加入路径
                pathList.append((r,c))
                # move到下个点
                r=nr
                c=nc
                if (r,c) == stopPoint:
                    # 终点加入路径
                    pathList.append((r,c))
                    findEndPoint=True
                else:
                    grids[r][c]=maze.VISIT
            else:
                (r,c) = pathList.pop()



        screen.blit(background, (0, 0))
        # 格子
        for cx in range(cols):
            for ry in range(rows):
                px,py=POSX + 1 + (cx) * DIAMOND_SIZE[0], POSY + 1 + (ry) * DIAMOND_SIZE[1]
                # 标记访问过的格子
                if maze.VISIT == grids[ry][cx]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREY, (px, py))
        
        if pathList:
            # 路径
            for pos in pathList:
                px,py=POSX + 1 + (pos[1]) * DIAMOND_SIZE[0], POSY + 1 + (pos[0]) * DIAMOND_SIZE[1]
                screen.blit(DIAMOND_GREEN, (px, py))
            # 当前r,c 
            px,py=POSX + 1 + (c) * DIAMOND_SIZE[0], POSY + 1 + (r) * DIAMOND_SIZE[1]
            screen.blit(DIAMOND_RED, (px, py))
        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (POSX + 0, POSY + 0, 20*cols+1, 20*rows+1), 2)
        # 画没打通的墙
        for cx in range( cols):
            for ry in range(rows):
                px,py=POSX + 1 + (cx) * DIAMOND_SIZE[0], POSY + 1 + (ry) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_BLACK]
                color2 = COLOR[COLOR_GREY]
                color2 = COLOR[COLOR_RED]
                color3 = COLOR[COLOR_GREY]
                if maze.WALL == walls[ry][cx][0]:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                if maze.WALL == walls[ry][cx][1]:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)
                #if 2 == walls[ry][cx][0]:
                #    pygame.draw.line(screen, color2, (px, py), (px, py+20), 2)
                #if 2 == walls[ry][cx][1]:
                #    pygame.draw.line(screen, color2, (px, py), (px+20, py), 2)
                #if 1 == walls[ry][cx][0]:
                #    pygame.draw.line(screen, color3, (px, py), (px, py+20), 2)
                #if 1 == walls[ry][cx][1]:
                #    pygame.draw.line(screen, color3, (px, py), (px+20, py), 2)
        # 
        if findEndPoint:
            # score_surface = use_font.render("找到终点", True, COLOR[COLOR_BLACK], COLOR[COLOR_GREY])
            screen.blit(score_surface, (POSX+50, POSY+rows*22))
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    depth_pathfinding_demo(20, 30)
