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
COLOR_RED, COLOR_BLUE, COLOR_GREEN, COLOR_YELLOW, COLOR_BLACK, COLOR_FLAXEN, COLOR_GOLDEN, COLOR_GRAY = list(range(
    diamond_color_size))
COLOR = {
    COLOR_RED: (255, 0, 0), # 红
    COLOR_BLUE: (0, 0, 255), # 蓝
    COLOR_GREEN: (0, 255, 0), # 绿
    COLOR_YELLOW: (255, 255, 0), # 黄
    COLOR_BLACK: (0, 0, 0), # 黑
    COLOR_FLAXEN: (250, 240, 230), # 亚麻
    COLOR_GOLDEN : (255,215,0), # 金
    COLOR_GRAY: (128,128,128), # 灰
}
# 格子大小
DIAMOND_LEN = 20
DIAMOND_SIZE = (DIAMOND_LEN, DIAMOND_LEN)
# 蓝格子
DIAMOND_BULE=pygame.surface.Surface(DIAMOND_SIZE).convert()
DIAMOND_BULE.fill(COLOR[COLOR_BLUE])
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
DIAMOND_GRAY.fill(COLOR[COLOR_FLAXEN])

# 各色的格子
DIAMONDS=[]
for x in range(diamond_color_size):
    diamoand=pygame.surface.Surface(DIAMOND_SIZE).convert()
    diamoand.fill(COLOR[x])
    DIAMONDS.append(diamoand)

# 字体
use_font = pygame.font.Font("FONT.TTF", 16)
use_font12 = pygame.font.Font("FONT.TTF", 12)
# 背景
background=pygame.surface.Surface(size).convert()
background.fill(COLOR[COLOR_BLACK])
# 文字
score_surface = use_font.render("找到终点", True, COLOR[COLOR_BLACK], COLOR[COLOR_FLAXEN])
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
INFINITE = maze.INFINITE # 无穷远


# 下一圈
def FindNextCircle(startList, walls, grids, rows, cols):
    startNextList = [] # 下一步
    for node in startList:
        r, c = node
        l = grids[r][c]
        # 可以到达的位置
        if r>0 and NOWALL == walls[r][c][1] and INFINITE == grids[r-1][c]:
            # move = 'u'
            nr=r-1
            nc=c
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
        if c>0 and NOWALL == walls[r][c][0] and INFINITE == grids[r][c-1]:
            # move = 'l'
            nr=r
            nc=c-1
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
        if c<cols-1 and NOWALL == walls[r][c+1][0] and INFINITE == grids[r][c+1] :
            # move='r'
            nr=r
            nc=c+1
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
        if r<rows-1 and NOWALL == walls[r+1][c][1] and INFINITE == grids[r+1][c] :
            # move='d'
            nr=r+1
            nc=c
            if (nr,nc) not in startNextList:
                startNextList.append((nr,nc))
                grids[nr][nc] = l+1
    # 下一圈
    startList.clear()
    startList.extend(startNextList)
    return startList


# 画方块
def draw_diamond(r,c, screen, POSX, POSY, diamod):
    px,py=POSX + 1 + (c) * DIAMOND_SIZE[0], POSY + 1 + (r) * DIAMOND_SIZE[1]
    screen.blit(diamod, (px, py))
    return 

# 画方块和字符串string
def draw_diamond_and_str(r,c, screen, POSX, POSY, diamod, use_font, string, color, color_back):
    px,py=POSX + 1 + (c) * DIAMOND_SIZE[0], POSY + 1 + (r) * DIAMOND_SIZE[1]
    screen.blit(diamod, (px, py))
    distance_surface = use_font.render(string, True, color, color_back)
    screen.blit(distance_surface, (px, py))
    return 


# 拆分迷宫
def split_maze_demo(walls, grids, startPoint, endPoint, startMap, endMap, rows, cols):
    startList = [startPoint]
    endList = [endPoint]
    startMap.append(startPoint)
    endMap.append(endPoint)
    while startList or endList:
        split_one_maze_demo(walls, grids, startList, endList, startMap, endMap, rows, cols)
    return startMap, endMap


# 一步一步执行
def split_one_maze_demo(walls, grids, startList, endList, startMap, endMap, rows, cols):
    # 起点
    FindNextCircle(startList, walls, grids, rows, cols)
    startMap+=startList
    # 终点
    FindNextCircle(endList, walls, grids, rows, cols)
    endMap+=endList
    return startList, endList



# Sample algorithm
def multipath_maze_demo(rows, cols):
    #walls = maze.aldous_broder_maze(rows, cols)
    #walls = maze.depth_maze(rows, cols)
    #walls = maze.kruskal_maze(rows, cols)
    #walls = maze.prim_maze(rows, cols)
    #walls = maze.wilson_maze(rows, cols)
    walls = maze.wilson_maze(rows, cols)
    POSX=40
    POSY=40
    # 初始化未访问
    grids=[[ INFINITE for i in range(cols)]for j in range(rows)]
    # 起点
    # 标记迷宫
    r=0
    c=0
    findEndPoint=False
    findPath=False
    # 起点
    startPoint=(r,c)
    # 终点
    endPoint=(rows-1,cols-1)
    mainList=[] # 主路径
    # 
    startList=[startPoint]
    endList=[endPoint]
    grids[startPoint[0]][startPoint[1]]=0 # 标记已经到过格子距离
    grids[endPoint[0]][endPoint[1]]=0
    # 没有访问过的格子
    notUseGrids = [] 
    for tr in range(rows):
        for tc in range(cols):
            notUseGrids.append((tr,tc))
    # 
    startMap=[]
    endMap=[]
    startMap += startList
    endMap += endList
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        if startList or endList:    
            # 分区
            # python 传参是引用传递 （不可改变参数指向，可改变参数的内部值。）
            # 可变对象：列表，字典（当参数时，函数内部的修改可以带出外部；但是赋值操作不能带出，此时的赋值操作相当于不可变对象的赋值）
            # 不可变的对象：数字，元组，字符串（当参数时，函数内部的修改不能带出；不可变对象修改值时相当于修改指向地址。）
            split_one_maze_demo(walls, grids, startList, endList, startMap, endMap, rows, cols)
            # 
            # split_maze_demo(walls, grids, startPoint, endPoint, startMap, endMap, rows, cols)
        elif not findPath:
            # 找需要拆的墙
            findPath
        else:
            findPath

        screen.blit(background, (0, 0))
        # 格子
        for cx in range(cols):
            for ry in range(rows):
                px,py=POSX + 1 + (cx) * DIAMOND_SIZE[0], POSY + 1 + (ry) * DIAMOND_SIZE[1]
                # 标记访问过的格子
                if maze.INFINITE == grids[ry][cx]:
                    draw_diamond(ry, cx, screen, POSX, POSY, DIAMOND_GRAY)
                else:
                    s = "{}".format(grids[ry][cx])
                    draw_diamond_and_str(ry, cx, screen, POSX,POSY, DIAMOND_GRAY, use_font12, s, COLOR[COLOR_BLACK], COLOR[COLOR_FLAXEN]) 
        # 圈地
        for pos in startMap:
            s = "{}".format(grids[pos[0]][pos[1]])
            draw_diamond_and_str(pos[0], pos[1], screen, POSX,POSY, DIAMOND_GREEN, use_font12, s, COLOR[COLOR_BLACK], COLOR[COLOR_GREEN])
        for pos in endMap:
            s = "{}".format(grids[pos[0]][pos[1]])
            draw_diamond_and_str(pos[0], pos[1], screen, POSX,POSY, DIAMOND_YELLOW, use_font12, s, COLOR[COLOR_BLACK], COLOR[COLOR_YELLOW])
        # 循环外圈
        if startList and not mainList:
            for pos in startList:
                s = "{}".format(grids[pos[0]][pos[1]])
                draw_diamond_and_str(pos[0], pos[1], screen, POSX,POSY, DIAMOND_RED, use_font12, s, COLOR[COLOR_BLACK], COLOR[COLOR_RED])
            for pos in endList:
                s = "{}".format(grids[pos[0]][pos[1]])
                draw_diamond_and_str(pos[0], pos[1], screen, POSX,POSY, DIAMOND_RED, use_font12, s, COLOR[COLOR_BLACK], COLOR[COLOR_RED])
        # 路径
        if mainList:
            for pos in mainList:
                s = "{}".format(grids[pos[0]][pos[1]])
                draw_diamond_and_str(pos[0], pos[1], screen, POSX,POSY, DIAMOND_YELLOW, use_font12, s, COLOR[COLOR_BLACK], COLOR[COLOR_YELLOW])
            # r,c
            px,py=POSX + 1 + (c) * DIAMOND_SIZE[0], POSY + 1 + (r) * DIAMOND_SIZE[1]
            screen.blit(DIAMOND_GREEN, (px, py))
            s = "{}".format(grids[r][c])
            distance_surface = use_font12.render(s, True, COLOR[COLOR_BLACK], COLOR[COLOR_GREEN])
            screen.blit(distance_surface, (px, py))

        # 画外墙
        pygame.draw.rect(screen, COLOR[COLOR_RED], (POSX + 0, POSY + 0, DIAMOND_LEN*cols+1, DIAMOND_LEN*rows+1), 2)
        # 画没打通的墙
        for cx in range( cols):
            for ry in range(rows):
                px,py=POSX + 1 + (cx) * DIAMOND_SIZE[0], POSY + 1 + (ry) * DIAMOND_SIZE[1]
                color = COLOR[COLOR_BLACK]
                if maze.WALL == walls[ry][cx][0]:
                    pygame.draw.line(screen, color, (px, py), (px, py+DIAMOND_LEN), 2)
                if maze.WALL == walls[ry][cx][1]:
                    pygame.draw.line(screen, color, (px, py), (px+DIAMOND_LEN, py), 2)
        # 打印文字提示
        if findEndPoint:
            screen.blit(score_surface, (POSX+50, POSY+rows*22))
        # 帧率
        clock.tick(25)

        pygame.display.update()
    return 

# main
if __name__ == "__main__":
    '''main'''
    multipath_maze_demo(20, 30)
