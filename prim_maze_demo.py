#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
# Randomized Prim's algorithm
#1.Start with a grid full of walls.
#2.Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
#3.While there are walls in the list:
#	1.Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
#		1.Make the wall a passage and mark the unvisited cell as part of the maze.
#		2.Add the neighboring walls of the cell to the wall list.
#	2.Remove the wall from the list.
# 随机普里姆算法
# 1。从布满墙壁的网格开始。
# 2。选一个细胞，把它标记为迷宫的一部分。将单元格的墙添加到墙列表中。
# 3。名单上有墙:
#   1。从列表中随机选择一面墙。如果细胞壁分裂的两个细胞中只有一个被访问，那么:
#       1。将墙壁做成通道，并将未造访的牢房标记为迷宫的一部分。
#       2。将单元格相邻的墙添加到墙列表中。
# 2。把墙从列表中移除。
# pygame
pygame.init()  # 初始化pygame
size = width, height = 800, 600  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
# 颜色
diamond_color_size = 7
COLOR_RED, COLOR_BLUE, COLOR_GREEN, COLOR_YELLOW, COLOR_BLACK, COLOR_GREY, COLOR_NO_DIAMOND = list(range(
    diamond_color_size))
COLOR = {
    COLOR_RED: (255, 0, 0),
    COLOR_BLUE: (0, 0, 255),
    COLOR_GREEN: (0, 255, 0),
    COLOR_YELLOW: (255, 255, 0),
    COLOR_BLACK: (0, 0, 0),
    COLOR_GREY: (250, 240, 230),
    COLOR_NO_DIAMOND: (100, 100, 100),
}
# 格子大小
DIAMOND_SIZE = (20, 20)
# 格子
DIAMOND=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND.fill(COLOR[1])

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

def draw_grid(lw, surface, rgb_color):
    rect = (lw, lw, DIAMOND_SIZE[0] -2*lw, DIAMOND_SIZE[1] -2*lw)
    pygame.draw.line(surface, rgb_color, (rect[0], rect[1]), (rect[0], rect[3]), lw)
    pygame.draw.line(surface, rgb_color, (rect[0], rect[1]), (rect[2], rect[1]), lw)
    pygame.draw.line(surface, rgb_color, (rect[0], rect[3]), (rect[2], rect[3]), lw)
    pygame.draw.line(surface, rgb_color, (rect[2], rect[1]), (rect[2], rect[3]), lw)
    return

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
#draw_grid(2, DIAMOND, (128, 128, 128))
# 背景
background=pygame.surface.Surface(size).convert()
background.fill(COLOR[COLOR_BLUE])

# 时间
clock = pygame.time.Clock()


# 随机墙
def prim_maze_demo(rows, cols):
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ ['|','-'] for i in range(cols+1)]for i in range(rows+1)]
    # 已访问标记
    way=[[ 0 for i in range(cols)]for i in range(rows)]
    # 设置起点
    r=0
    c=0
    # 起点加入记录
    # 标记为迷宫的一部分
    way[r][c]=1
    # 墙列表
    walllist=[]
    walllist.append((r+1,c,'-'))
    walllist.append((r,c+1,'|'))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if walllist:
            # 随机选一个墙
            r, c, d = random.choice(walllist)
            rr,cc,dd=r,c,d
            # 移除墙
            walllist.remove((r,c,d))
            if d == '|':
                # 如果这面墙分隔的两个单元格只有一个单元格被访问过，那么：
                if c > 0 and (not way[r][c-1] == way[r][c] ):
                    #1.把墙打通，将未访问的单元格标记成为迷宫的一部分
                    wall[r][c][0]=0
                    if way[r][c] == 1:
                        nc=c-1
                    else:
                        nc=c
                    c=nc
                    way[r][c]=1
                    #2.将单元格相邻的墙加入到墙列表中
                    # 上
                    if r > 0 and wall[r][c][1] == '-':
                        walllist.append((r,c,'-'))
                    # 下
                    if r+1 < rows and wall[r+1][c][1] == '-':
                        walllist.append((r+1,c,'-'))
                    # 左
                    if c > 0 and wall[r][c][0] == '|':
                        walllist.append((r,c,'|'))
                    # 右
                    if c+1 < cols and wall[r][c+1][0] == '|':
                        walllist.append((r,c+1,'|'))
            elif d == '-':
                # 如果这面墙分隔的两个单元格只有一个单元格被访问过，那么：
                if r > 0 and ( (not way[r-1][c]) == way[r][c] ):
                    #1.把墙打通，将未访问的单元格标记成为迷宫的一部分
                    wall[r][c][1]=0
                    if way[r][c] == 1:
                        nr=r-1
                    else:
                        nr=r
                    r=nr
                    way[r][c]=1
                    #2.将单元格相邻的墙加入到墙列表中
                    # 上
                    if r > 0 and wall[r][c][1] == '-':
                        walllist.append((r,c,'-'))
                    # 下
                    if r + 1 < rows and wall[r+1][c][1] == '-':
                        walllist.append((r+1,c,'-'))
                    # 左
                    if c > 0 and wall[r][c][0] == '|':
                        walllist.append((r,c,'|'))
                    # 右
                    if c + 1 < cols and wall[r][c+1][0] == '|':
                        walllist.append((r,c+1,'|'))
            #2.如果墙两面的单元格都已经被访问过，那就从列表里移除这面墙
            for rrr1, ccc1, ddd1 in walllist:
                if ddd1 == '|':
                    if ccc1 > 0 and way[rrr1][ccc1-1] == 1 and way[rrr1][ccc1] == 1:
                        walllist.remove((rrr1,ccc1,ddd1))
                elif ddd1 == '-':
                    if rrr1 > 0 and way[rrr1-1][ccc1] == 1 and way[rrr1][ccc1] == 1:
                        walllist.remove((rrr1,ccc1,ddd1))

        screen.blit(background, (0, 0))
        # 画格子
        for x in range(cols):
            for y in range(rows):
                px,py=1 + (x) * DIAMOND_SIZE[0], 1 + (y) * DIAMOND_SIZE[1]
                # 标记走过的
                if way[y][x]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREY, (px, py))

        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*cols+1, 20*rows+1), 2)
        # 画没打通的墙
        for x in range( cols):
            for y in range(rows):
                px,py=1 + (x) * DIAMOND_SIZE[0], 1 + (y) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_BLACK]
                if wall[y][x][0]:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                if wall[y][x][1]:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)
        
        # 画记录列表里的墙记
        for rrr,ccc,ddd in walllist:
            px,py=1 + (ccc) * DIAMOND_SIZE[0], 1 + (rrr) * DIAMOND_SIZE[1]
            color = (255,50,255)
            if ddd == '|':
                pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
            else:
                pygame.draw.line(screen, color, (px, py), (px+20, py), 2)
        # 画刚被打通的墙
        if walllist:
            px,py=1 + (cc) * DIAMOND_SIZE[0], 1 + (rr) * DIAMOND_SIZE[1]
            color = (255,215,0)
            if dd == '|':
                pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
            else:
                pygame.draw.line(screen, color, (px, py), (px+20, py), 2)
        # 
        if not walllist:
            score_surface = use_font.render("生成完成！", True, COLOR[COLOR_BLACK], COLOR[COLOR_GREY])
            screen.blit(score_surface, (50, rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    prim_maze_demo(20, 30)
