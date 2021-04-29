#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
import maze 
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

# 访问过的格子 
DIAMOND_GREEN=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_GREEN.fill(COLOR[COLOR_GREEN])
# 访问过的格子 
DIAMOND_RED=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_RED.fill(COLOR[COLOR_RED])

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


def depth_maze_demo(rows, cols):
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][0][1]横墙
    # 左[0]竖墙，上[1]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [WALL,WALL] for i in range(cols)]for i in range(rows)]
    # way用来标记已经访问过的格子
    # 初始化全未访问
    way=[[ NOVISIT for i in range(cols)]for i in range(rows)]
    # 设置起点
    r=0
    c=0
    # 起点加入记录
    history = [(r,c)]
    # 1。选择初始单元格，将其标记为已访问，并将其压入堆栈
    # 2。堆栈不是空的
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if history:
            way[r][c] = VISIT #
            check = []
            # 可以移动到的位置
            if c > 0 and way[r][c-1] == NOVISIT:
                check.append('L')  
            if r > 0 and way[r-1][c] == NOVISIT:
                check.append('U')
            if c < cols-1 and way[r][c+1] == NOVISIT:
                check.append('R')
            if r < rows-1 and way[r+1][c] == NOVISIT:
                check.append('D')    
            # 如果当前单元有任何未被访问的邻居
            if len(check): 
                # 选择一个未被拜访的邻居
                # 移除当前单元格和所选单元格之间的墙
                # 将选中的单元格标记为已访问的，并将其压入堆栈
                history.append((r, c))
                # 随机移动
                move_direction = random.choice(check)
                # 打通墙壁
                if move_direction == 'L':
                    wall[r][c][0] = NOWALL
                    c=c-1
                if move_direction == 'U':
                    wall[r][c][1] = NOWALL
                    r=r-1
                if move_direction == 'R':
                    c=c+1
                    wall[r][c][0] = NOWALL
                if move_direction == 'D':
                    r=r+1
                    wall[r][c][1] = NOWALL
            else: 
                #从堆栈中弹出一个单元格并使其成为当前单元格
                r, c = history.pop()
        # 
        screen.blit(background, (0, 0))
        # 格子
        for x in range(cols):
            for y in range(rows):
                px,py=1 + x * DIAMOND_SIZE[0], 1 + y * DIAMOND_SIZE[1]
                # 标记走过的
                if NOVISIT == way[y][x]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GRAY, (px, py))
        
        px,py=1 + c * DIAMOND_SIZE[0], 1 + r * DIAMOND_SIZE[1]
        screen.blit(DIAMOND_RED, (px, py))
        # 墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*cols+1, 20*rows+1), 2)
        # 
        for x in range(cols):
            for y in range(rows):
                px,py=1 + x * DIAMOND_SIZE[0], 1 + y * DIAMOND_SIZE[1]
                if WALL == wall[y][x][0]:
                    pygame.draw.line(screen, COLOR[COLOR_BLACK], (px, py), (px, py+20), 2)
                if WALL ==  wall[y][x][1]:
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
