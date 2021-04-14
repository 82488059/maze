#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
import random
import pygame
#Aldous-Broder algorithm
#The Aldous-Broder algorithm also produces uniform spanning trees.

# 1.Pick a random cell as the current cell and mark it as visited.
# 2.While there are unvisited cells:
#   1.Pick a random neighbour.
#   2.If the chosen neighbour has not been visited:
#       1.Remove the wall between the current cell and the chosen neighbour.
#       2.Mark the chosen neighbour as visited.
#   3.Make the chosen neighbour the current cell.

# Aldous-Broder算法
# Aldous-Broder算法也生成统一的生成树。
# 1。选择一个随机的单元格作为当前单元格，并将其标记为已访问的。
# 2。当存在未访问细胞时:
#   1。随机选择一个邻居。
#   2。如果选中的邻居没有被访问:
#       1。移除当前单元格和所选邻居之间的墙。
#       2。标记被选中的邻居已被拜访过。
#   3。使选择的邻居成为当前单元格。

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
# 行列
num_cols=30 #
num_rows=20 #
# 背景
background=pygame.surface.Surface(((num_cols ) * DIAMOND_SIZE[0] + 2 , (num_rows ) * DIAMOND_SIZE[1] + 2)).convert()
background.fill(COLOR[COLOR_BLUE])
# 时间
clock = pygame.time.Clock()

##############################################
#   格子访问标记x,y,0，右墙x,y,1，下墙x,y,2
##############################################

def aldous_broder_maze(rows, cols):
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化未访问，墙未打通
    grids=[[ [0] for i in range(cols)]for j in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(cols)]for i in range(rows)]
    notusegrids = [] # 没有访问过的格子
    for tr in range(rows):
        for tc in range(cols):
            notusegrids.append((tr,tc))
    # 选择一个随机的单元格作为当前单元格，并将其标记为已访问的。
    r,c = random.choice(notusegrids)
    # 标记迷宫
    grids[r][c][0]=1
    notusegrids.remove((r,c))
    # 当存在未访问细胞时:
    while notusegrids:
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
                opwall=(r, c, 1)
            if move == 'l':
                newr = r
                newc = c-1
                opwall=(r, c, 0)
            if move == 'd':
                newr = r+1
                newc = c
                opwall=(newr, newc, 1)
            if move == 'r':
                newr = r
                newc = c+1
                opwall=(newr, newc, 0)
            # 如果选中的邻居没有被访问:
            if grids[newr][newc][0] == 0:
                #   1。移除当前单元格和所选邻居之间的墙。
                #   2。标记被选中的邻居已被拜访过。
                #   3。使选择的邻居成为当前单元格。
                grids[newr][newc][0]=1
                notusegrids.remove((newr,newc))
                wall[opwall[0]][opwall[1]][opwall[2]] = 1
                r=newr
                c=newc   
            else:
                # 使选择的邻居成为当前单元格。
                r=newr
                c=newc 
    return wall

# 随机格子
def aldous_broder_maze_demo(rows, cols):
    # 初始化未访问，墙未打通
    grids=[[ [0] for i in range(cols)]for j in range(rows)]
    # 一个格子有四堵墙，其中有两面共有，用2个标记就够用。
    # 墙0通路1。x,y是墙的坐标。
    # wall[x][y][0]竖墙wall[x][y][1]横墙
    # 墙 [0]表示格子访问标记，左[1]竖墙，上[2]横墙，最右边竖墙和最下边横墙没有记录。
    # (最左和最上墙不能打通，r,c右和r,c+1左共用墙。r,c和r+1,c共用横墙)
    # 初始化全为墙
    wall=[[ [0,0] for i in range(num_cols)]for i in range(num_rows)]

    notusegrids = [] # 没有访问过的格子
    for tr in range(rows):
        for tc in range(cols):
            notusegrids.append((tr,tc))
    # 选择一个随机的单元格作为当前单元格，并将其标记为已访问的。
    r,c = random.choice(notusegrids)
    # 标记迷宫
    grids[r][c][0]=1
    notusegrids.remove((r,c))
    #wall = aldous_broder_maze(rows, cols)
    #notusegrids=[]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # 当存在未访问细胞时:
        if  notusegrids:
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
                    opwall=(r, c, 1)
                if move == 'l':
                    newr = r
                    newc = c-1
                    opwall=(r, c, 0)
                if move == 'd':
                    newr = r+1
                    newc = c
                    opwall=(newr, newc, 1)
                if move == 'r':
                    newr = r
                    newc = c+1
                    opwall=(newr, newc, 0)
                # 如果选中的邻居没有被访问:
                if grids[newr][newc][0] == 0:
                    #   1。移除当前单元格和所选邻居之间的墙。
                    #   2。标记被选中的邻居已被拜访过。
                    #   3。使选择的邻居成为当前单元格。
                    grids[newr][newc][0]=1
                    notusegrids.remove((newr,newc))
                    wall[opwall[0]][opwall[1]][opwall[2]] = 1
                    r=newr
                    c=newc   
                else:
                    # 使选择的邻居成为当前单元格。
                    r=newr
                    c=newc 

        screen.blit(background, (0, 0))
        # 格子
        for cx in range(num_cols):
            for ry in range(num_rows):
                px,py=1 + (cx) * DIAMOND_SIZE[0], 1 + (ry) * DIAMOND_SIZE[1]
                # 标记访问过的格子
                if grids[ry][cx][0]:
                    screen.blit(DIAMOND, (px, py))
                else:
                    screen.blit(DIAMOND_GREY, (px, py))
        # 当前点
        if notusegrids:
            px,py=1 + (c) * DIAMOND_SIZE[0], 1 + (r) * DIAMOND_SIZE[1]
            screen.blit(DIAMOND_GREEN, (px, py))

        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (0, 0, 20*num_cols+1, 20*num_rows+1), 2)
        # 画墙
        for cx in range( num_cols):
            for ry in range(num_rows):
                px,py=1 + (cx) * DIAMOND_SIZE[0], 1 + (ry) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_BLACK]
                if not wall[ry][cx][0]:
                    pygame.draw.line(screen, color, (px, py), (px, py+20), 2)
                if not wall[ry][cx][1]:
                    pygame.draw.line(screen, color, (px, py), (px+20, py), 2)

        # 
        if not notusegrids:
            score_surface = use_font.render("生成完成！", True, COLOR[COLOR_BLACK], COLOR[COLOR_GREY])
            screen.blit(score_surface, (50, num_rows*22))
        
        time_passed = clock.tick(30)

        pygame.display.update()
    return 



# main
if __name__ == "__main__":
    '''main'''
    aldous_broder_maze_demo(20, 30)
