import pygame
from random import choice
from copy import deepcopy


# from settings import *

class Figure:
    figures_pos = [[(-1, 0), (-2, 0), (0, 0), (1, 0)],
                   [(0, -1), (-1, -1), (-1, 0), (0, 0)],
                   [(-1, 0), (-1, 1), (0, 0), (0, -1)],
                   [(0, 0), (-1, 0), (0, 1), (-1, -1)],
                   [(0, 0), (0, -1), (0, 1), (-1, -1)],
                   [(0, 0), (0, -1), (0, 1), (-1, -1)],
                   [(0, 0), (0, -1), (0, 1), (-1, 0)]]  # 7 figures

    figures = [[pygame.Rect(x + 3, y + 1, 1, 1) for x, y in fig_pos] for fig_pos in figures_pos]

    def __init__(self, screen, block_size, block_count, grid):
        # self.figure = choice(self.figures)
        self.rect = pygame.Rect(0, 0, block_size - 2, block_size - 2)
        self.figure = deepcopy(choice(self.figures))
        self.block_size = block_size
        self.screen = screen
        self.direction = (0, 1)
        # self.draw()
        self.speed = 50
        self.speed_count = 0
        self.speed_limit = 49
        self.block_count = block_count
        self.grid = grid
        self.last_update = 0
        self.dx = 0

        # print(self.figures)

    def draw(self):
        for i in range(4):
            self.rect.x = self.figure[i].x * self.block_size
            self.rect.y = self.figure[i].y * self.block_size
            pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

    def move_with_check_borders(self, dt):
        self.move_x_with_check_borders(dt)
        self.move_y_with_check_borders(dt)

    def move_x_with_check_borders(self, dt):
        old_figure = deepcopy(self.figure)
        for i in range(4):
            self.figure[i].x += self.dx
            if self.check_block_borders(self.figure[i]):
                self.figure = deepcopy(old_figure)
                break

            # if self.figure[i].x < 0 or self.figure[i].x == self.block_count[0]:
            #     self.figure = deepcopy(old_figure)
            #     break

    def move_y_with_check_borders(self, dt):
        old_figure = deepcopy(self.figure)
        # self.last_update += dt
        for i in range(4):
            self.figure[i].y += 1
            if self.check_block_borders(self.figure[i]):
                self.add_to_grid(old_figure)
                # self.figure = deepcopy(old_figure)
                self.figure = deepcopy(choice(self.figures))
                break


    def check_block_borders(self, block):
        if block.y == self.block_count[1] or self.grid[block.y][block.x]:
            return True
        elif block.x < 0 or block.x == self.block_count[0]:
            return True

    # def check_borders(self):
    #     for i in range(4):
    #         if self.figure[i].y == self.block_count[1] or self.grid[self.figure[i].y][self.figure[i].x]:
    #             return True
    #
    #         elif self.figure[i].x < 0 or self.figure[i].x == self.block_count[0]:
    #             return True


                # self.add_to_grid(old_figure)
            # self.figure = deepcopy(choice(self.figures))
            #     break

    def update(self, keys, dt):
        self.dx = 0
        if keys[pygame.K_LEFT]:
            self.dx = -1

        if keys[pygame.K_RIGHT]:
            self.dx = 1

        if keys[pygame.K_DOWN]:
            print('ДОДЕЛАТЬ')

        # self.move_with_check_borders(dt)

        # if self.last_update >= 100:
        #     self.last_update = 0
        #     self.speed_count = 0
        self.move_with_check_borders(dt)

        # self.move()
        # if self.check_borders():
        #     self.figure = old_figure

    def add_to_grid(self, figure):
        for i in range(4):
            if figure[i].y <= 0:
                print('GAME OVER')
                exit()

            self.grid[figure[i].y][figure[i].x] = 1
                #print(figure[i].y, figure[i].x)









    # self.direction = (0, 1)
            # print(self.grid[figure[i].y - 1][figure[i].x])
    # if keys[pygame.K_LEFT]:
    #     self.direction = (-1, 1)
    # elif keys[pygame.K_RIGHT]:
    #     self.direction = (1, 1)
    # elif keys[pygame.K_DOWN]:
    #     self.direction = (0, 2)
    # self.move()
    # self.check_borders()

    # self.figure[i].x += 1
    # self.draw()
