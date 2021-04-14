#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
#
# Randomized depth-first search
# Recursive implementation
#1。Choose the initial cell, mark it as visited and push it to the stack
#2。While the stack is not empty
#   1。Pop a cell from the stack and make it a current cell
#   2。If the current cell has any neighbours which have not been visited
#       1。Push the current cell to the stack
#       2。Choose one of the unvisited neighbours
#       3。Remove the wall between the current cell and the chosen cell
#       4。Mark the chosen cell as visited and push it to the stack
#随机深度优先搜索
#递归实现
#1。选择初始单元格，将其标记为已访问，并将其压入堆栈
#2。而堆栈不是空的
#   1。从堆栈中弹出一个单元格并使其成为当前单元格
#   2。如果当前单元有任何未被访问的邻居
#       1。将当前单元格压入堆栈
#       2。选择一个未被拜访的邻居
#       3。移除当前单元格和所选单元格之间的墙
#       4。将选中的单元格标记为已访问的，并将其压入堆栈

# pygame
pygame.init()  # 初始化pygame
size = width, height = 800, 600  # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
# 行列
num_cols=30
num_rows=20

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
background=pygame.surface.Surface(size).convert()
background.fill(COLOR[COLOR_BLUE])

# 时间
clock = pygame.time.Clock()

# 墙不占用单元格
# 可以保证所有的格都是相通的
# 深度优先算法可以遍历所有的单元格。
# Randomized depth-first search
# Recursive backtracker
# 递归回溯算法
def depth_maze(rows, cols):
    history = [(0,0)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][0][1]横墙
    # 左[0]竖墙，上[1]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
    # way用来标记已经访问过的格子
    # 初始化全未访问
    way=[[ 0 for i in range(cols)]for i in range(rows)]
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化未访问，墙未打通
    r=0
    c=0
    # 1。选择初始单元格，将其标记为已访问，并将其压入堆栈
    # 2。堆栈不是空的
    while history:
        way[r][c] = 1 # 
        check = []
        if c > 0 and way[r][c-1] == 0:
            check.append('L')  
        if r > 0 and way[r-1][c] == 0:
            check.append('U')
        if c < cols-1 and way[r][c+1] == 0:
            check.append('R')
        if r < rows-1 and way[r+1][c] == 0:
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
    return wall


def depth_maze_demo(rows, cols):
    history = [(0,0)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][0][1]横墙
    # 左[0]竖墙，上[1]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
    # way用来标记已经访问过的格子
    # 初始化全未访问
    way=[[ 0 for i in range(cols)]for i in range(rows)]
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化未访问，墙未打通
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
            if c < cols-1 and way[r][c+1] == 0:
                check.append('R')
            if r < rows-1 and way[r+1][c] == 0:
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
        # 格子
        for x in range(cols):
            for y in range(rows):
                px,py=1 + x * DIAMOND_SIZE[0], 1 + y * DIAMOND_SIZE[1]
                # 标记走过的
                if way[y][x]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREEN, (px, py))
        
        px,py=1 + c * DIAMOND_SIZE[0], 1 + r * DIAMOND_SIZE[1]
        screen.blit(DIAMOND_RED, (px, py))
        # 墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*cols+1, 20*rows+1), 2)
        # 
        for x in range(cols):
            for y in range(rows):
                px,py=1 + x * DIAMOND_SIZE[0], 1 + y * DIAMOND_SIZE[1]
                if not wall[y][x][0]:
                    pygame.draw.line(screen, COLOR[COLOR_BLACK], (px, py), (px, py+20), 2)
                if not wall[y][x][1]:
                    pygame.draw.line(screen, COLOR[COLOR_BLACK], (px, py), (px+20, py), 2)
        if not history:
            score_surface = use_font.render("生成完成！", True, COLOR[COLOR_BLACK], COLOR[COLOR_BLUE])
            screen.blit(score_surface, (cols*22/10, rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    depth_maze_demo(20,30)
