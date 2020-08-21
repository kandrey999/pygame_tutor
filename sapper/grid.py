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
        self.bombs = []
        self.init_bombs()

        self.a = False


    def draw(self):
        [[block.draw() for block in row] for row in self.grid]

    def init_bombs(self):
        count_set_bombs = 0
        max_set_bombs = self.block_count[0] * self.block_count[1]

        if self.bombs_count > max_set_bombs:
            print(f'BOMBS LIMIT, BOMBS COUNT = {max_set_bombs}')
            self.bombs_count = max_set_bombs

        while count_set_bombs != self.bombs_count:
            block = self.grid[randrange(self.block_count[1])][randrange(self.block_count[0])]
            if not block.is_bomb:
                block.is_bomb = True
                count_set_bombs += 1
                self.bombs.append(block)
        # [print(block.pos) for block in self.bombs]

    def check_bombs_state(self):
        if sum([block.is_open for block in self.bombs]) > 0:
            self.open_all_bombs()

    def open_all_bombs(self):
        font = pygame.font.Font(pygame.font.match_font('arial'), 50)
        image = pygame.font.Font.render(font, '*', True, (255, 0, 0))
        [block.change_image(image) for block in self.bombs]
        self.a = True

        # for i in range(self.bombs_count):
        #     self.grid[randrange(self.block_count[1])][randrange(self.block_count[0])].is_bomb = True

    def check_mouse_click_on_blocks_and_calculate_bombs_near(self, mouse_keys: tuple, mouse_pos: tuple):
        if sum(mouse_keys) and sum(mouse_pos):
            mouse_rect = pygame.Rect(*mouse_pos, 1, 1)
            for y, row in enumerate(self.grid):
                for x, block in enumerate(row):
                    if mouse_rect.colliderect(block.rect):
                        return block, self.calculate_bombs_near_block((x, y))

    # def click_on_block_react(self, mouse_keys, mouse_pos):
    #     if sum(mouse_keys) > 0:

    # rect = self.image.get_rect()
    # self.image.fill((255, 255, 255))
    # if mouse[0]:
    #     if self.is_bomb:
    #         font = pygame.font.Font(pygame.font.match_font('arial'), 50)
    #         image = font.render('*', True, (255, 0, 0))
    #         self.image.blit(image, (self.size // 4, 0))
    #         print('bomb')
    #         # pygame.draw.rect(self.image, (255, 0, 0), rect)
    #     else:
    #         font = pygame.font.Font(pygame.font.match_font('arial'), 50)
    #         image = font.render(str(self.bombs_near), True, (0, 0, 255))
    #         self.image.blit(image, (self.size // 4, 0))
    #
    # elif mouse[2]:
    #     font = pygame.font.Font(pygame.font.match_font('arial'), 50)
    #     image = font.render('|>', True, (0, 255, 0))
    #     self.image.blit(image, (self.size // 4, 0))

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

        return sum
        # self.grid[y][x].bombs_near = sum

    def calculate_count_of_marked_blocks(self):
        s = 0
        for row in self.grid:
            for block in row:
                if block.is_marked:
                    s += 1
        # print(s)

    def update(self, mouse_keys, mouse_pos):
        clicked_block_and_bombs_near = self.check_mouse_click_on_blocks_and_calculate_bombs_near(mouse_keys, mouse_pos)
        if clicked_block_and_bombs_near:
            clicked_block, bombs_near_block = clicked_block_and_bombs_near
            clicked_block.react_on_click(mouse_keys, bombs_near_block)
            self.calculate_count_of_marked_blocks()

        self.check_bombs_state()

        if self.a:
            return self.a



            # self.block.change_image(image)
        # if self.check_mouse_click_on_blocks(mouse_keys, mouse_pos):
