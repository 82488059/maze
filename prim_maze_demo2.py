#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
#
#1.Make the initial cell the current cell and mark it as visited
#2.While there are unvisited cells
#	1.If the current cell has any neighbours which have not been visited
#		1.Choose randomly one of the unvisited neighbours
#		2.Push the current cell to the stack
#		3.Remove the wall between the current cell and the chosen cell
#		4.Make the chosen cell the current cell and mark it as visited
#	2.Else if stack is not empty
#		1.Pop a cell from the stack
#		2.Make it the current cell
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
# 行列
num_cols=30 #
num_rows=20 #
# 背景
background=pygame.surface.Surface(((num_cols ) * DIAMOND_SIZE[0] + 2 , (num_rows ) * DIAMOND_SIZE[1] + 2)).convert()
background.fill(COLOR[COLOR_BLUE])
# 时间
clock = pygame.time.Clock()


# 随机格子
def prim_maze_demo(rows, cols):
    # 墙 0表示通路 |竖墙 -横墙
    wall=[[ ['|','-'] for i in range(num_cols)]for i in range(num_rows)]
    # 已访问标记
    way=[[ 0 for i in range(num_cols)]for i in range(num_rows)]
    # 设置起点
    r=0
    c=0
    # 设置已经走过
    way[r][c]=1
    # 格子列表
    gridlist=[]
    gridlist.append((r,c))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if gridlist:
            # 随机选择一个格子
            r, c = random.choice(gridlist)
            # 
            #gridlist.remove((r,c))
            # 
            #way[r][c] = 1 # 
            check = []
            if c > 0 and way[r][c-1] == 0:
                check.append('L')  
            if r > 0 and way[r-1][c] == 0:
                check.append('U')
            if c < num_cols-1 and way[r][c+1] == 0:
                check.append('R')
            if r < num_rows-1 and way[r+1][c] == 0:
                check.append('D')    

            if len(check): 
                gridlist.append((r, c))
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


        screen.blit(background, (0, 0))
        # 格子
        for x in range(num_cols):
            for y in range(num_rows):
                px,py=1 + (x) * DIAMOND_SIZE[0], 1 + (y) * DIAMOND_SIZE[1]
                # 标记走过的
                if way[y][x]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREY, (px, py))

        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*num_cols+1, 20*num_rows+1), 2)
        # 画没打通的墙
        for x in range( num_cols):
            for y in range(num_rows):
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
            screen.blit(score_surface, (50, num_rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    prim_maze_demo(20, 30)
