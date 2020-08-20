import pygame
from random import randrange
from block import Block


class Grid:
    def __init__(self, screen: pygame.display, block_size: int, block_count, bombs_count):
        self.screen = screen
        self.block_size = block_size
        self.block_count = block_count
        # self.block_count = self.screen.w // self.block_size, self.screen.h // self.block_size
        self.bombs_count = bombs_count
        self.grid = [[Block(self.screen, (x * self.block_size, y * self.block_size), self.block_size) for x in
                      range(self.block_count[0] + 1)] for y in range(self.block_count[1] + 1)]
        self.init_bombs()

    def draw(self):
        [[block.draw() for block in row] for row in self.grid]

    def init_bombs(self):
        for i in range(self.bombs_count):
            self.grid[randrange(self.block_count[1])][randrange(self.block_count[0])].is_bomb = True

    def check_mouse_click(self, mouse_pos: tuple, mouse_click: tuple):
        mouse_rect = pygame.Rect(*mouse_pos, 1, 1)
        for y, row in enumerate(self.grid):
            for x, block in enumerate(row):
                if mouse_rect.colliderect(block.rect):
                    # print('collide')
                    self.calculate_bombs_near_block((x, y))
                    # print(self.grid[y][x].bombs_near)
                    block.mouse_click(mouse_click)

    def calculate_bombs_near_block(self, block_pos_in_grid):
        x, y = block_pos_in_grid
        sum = 0
        if self.grid[y - 1][x - 1].is_bomb: sum += 1
        if self.grid[y - 1][x].is_bomb: sum += 1
        if self.grid[y - 1][x + 1].is_bomb: sum += 1
        if self.grid[y][x - 1].is_bomb: sum += 1
        if self.grid[y][x + 1].is_bomb: sum += 1
        if self.grid[y + 1][x - 1].is_bomb: sum += 1
        if self.grid[y + 1][x].is_bomb: sum += 1
        if self.grid[y + 1][x + 1].is_bomb: sum += 1

        self.grid[y][x].bombs_near = sum

        print(sum)
