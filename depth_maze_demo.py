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
# 行列
num_cols=30
num_rows=20
# 墙0表示墙1表示通路[0]竖墙[1]横墙
wall=[[ [0,0] for i in range(num_cols)]for i in range(num_rows)]
# 已访问标记
way=[[ 0 for i in range(num_cols)]for i in range(num_rows)]
# 颜色
diamond_color_size = 6
COLOR_RED, COLOR_BLUE, COLOR_GREEN, COLOR_YELLOW, COLOR_BLACK, COLOR_NO_DIAMOND = list(range(
    diamond_color_size))
COLOR = {
    COLOR_RED: (255, 0, 0),
    COLOR_BLUE: (0, 0, 255),
    COLOR_GREEN: (0, 255, 0),
    COLOR_YELLOW: (255, 255, 0),
    COLOR_BLACK: (0, 0, 0),
    COLOR_NO_DIAMOND: (100, 100, 100),
}
# 格子大小
DIAMOND_SIZE = (20, 20)
# 格子
DIAMOND=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND.fill(COLOR[1])

# 访问过的格子 
DIAMOND_GREEN=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_GREEN.fill(COLOR[COLOR_GREEN])
# 访问过的格子 
DIAMOND_RED=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_RED.fill(COLOR[COLOR_RED])

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
background=pygame.surface.Surface(((num_cols ) * DIAMOND_SIZE[0] + 2 , (num_rows ) * DIAMOND_SIZE[1] + 2)).convert()
background.fill(COLOR[2])

# 记录        
history = [(0,0)]
# 时间
clock = pygame.time.Clock()

# 算法
# Recursive backtracker
def depth_maze():
    r=0
    c=0
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


def depth_maze_demo():
    global history
    global way
    global wall
    r=0
    c=0
    history = [(r,c)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        if history:
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
                r, c = history.pop()
        # 
        screen.blit(background, (0, 0))
        
        #screen.blit(background, (x, y))
        # 格子
        for x in range(num_cols):
            for y in range(num_rows):
                px,py=1 + x * DIAMOND_SIZE[0], 1 + y * DIAMOND_SIZE[1]
                # 标记走过的
                if way[y][x]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREEN, (px, py))
        
        px,py=1 + c * DIAMOND_SIZE[0], 1 + r * DIAMOND_SIZE[1]
        screen.blit(DIAMOND_RED, (px, py))

        # 墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*num_cols+1, 20*num_rows+1), 2)
        # 
        for x in range(num_cols):
            for y in range(num_rows):
                px,py=1 + x * DIAMOND_SIZE[0], 1 + y * DIAMOND_SIZE[1]
                if not wall[y][x][0]:
                    pygame.draw.line(screen, COLOR[COLOR_BLACK], (px, py), (px, py+20), 2)

                if not wall[y][x][1]:
                    pygame.draw.line(screen, COLOR[COLOR_BLACK], (px, py), (px+20, py), 2)
                
        if not history:
            score_surface = use_font.render("生成完成！", True, COLOR[COLOR_BLACK], COLOR[COLOR_BLUE])
            screen.blit(score_surface, (num_cols*22/10, num_rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    depth_maze_demo()
