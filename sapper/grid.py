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
        self.grid = [[Block(self.screen, (x, y), self.block_size) for x in
                      range(self.block_count[0] + 5)] for y in range(self.block_count[1] + 5)]
        self.bombs = []
        self.init_bombs()
        # self.calculate_bombs_near_block_in_grid()
        self.f()
        self.a = False

    @property
    def flatten(self):
        # for row in self.grid:
        #     for block in row:
        #         yield block
        for y in range(self.block_count[1]):
            for x in range(self.block_count[0]):
                yield self.grid[y][x]

    def f(self):
        for block in self.flatten:
            block.bombs_near = self.calculate_bombs_near_block(block)
            # self.calculate_bombs_near_block(block)
        # ((block.bombs_near = self.calculate_bombs_near_block(block)) for block in self.flatten)

    # def calculate_bombs_near_block_in_grid(self):
    #     for block in self.flatten:
    #         block.bombs_near = self.calculate_bombs_near_block(block)
        # [block.bombs_near = self.calculate_bombs_near_block_in_grid(block) for block in self.flatten]

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
        if not (sum(mouse_keys) and sum(mouse_pos)): return
        mouse_rect = pygame.Rect(*mouse_pos, 1, 1)
        for block in self.flatten:
            if mouse_rect.colliderect(block.rect):
                return block, self.calculate_bombs_near_block(block)


    def open_zero_blocks(self, block, bombs_near_block):
        if bombs_near_block == 0 and not block.is_open:
            print('i')
            # for a in self.get_neighbours(block):
            block.open_as_empty()
            [neighbour.open_as_empty() if neighbour.bombs_near == 0 else neighbour.open_as_normal() for neighbour in self.get_neighbours(block)]
            # [neighbour.open_as_normal() for neighbour in self.get_neighbours(block) if neighbour.bombs_near > 0]

            # Y ОЧЕНЬ ВЫСОКИЙ СТАНОВИТСЯ
            # [print(neighbour.bombs_near) for neighbour in self.get_neighbours(block) if neighbour.bombs_near == 0]
                # print(a.bombs_near)



    # def open_neighbours(self, block):
    #     block.open()
    #     [neighbour.open() for neighbour in self.get_neighbours(block)]



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

    def calculate_bombs_near_block(self, block):
        return sum(neighbour.is_bomb for neighbour in self.get_neighbours(block))


    def get_neighbours(self, block):
        x, y = block.grid_pos

        # print(x, y)
        yield self.grid[y - 1][x - 1]
        yield self.grid[y - 1][x]
        # print(x, y)
        yield self.grid[y - 1][x + 1]
        yield self.grid[y][x - 1]
        yield self.grid[y][x + 1]
        yield self.grid[y + 1][x - 1]
        yield self.grid[y + 1][x]
        yield self.grid[y + 1][x + 1]

        # self.grid[y][x].bombs_near = sum

    def calculate_count_of_marked_blocks(self):
        # s = 0
        # for row in self.grid:
        #     for block in row:
        #         if block.is_marked:
        #             s += 1
        # print(s)
        sum((block.is_marked for block in self.flatten))

    def update_blocks(self, mouse_keys, mouse_pos):
        clicked_block, bombs_near_block = None, None
        clicked_block_and_bombs_near = self.check_mouse_click_on_blocks_and_calculate_bombs_near(mouse_keys, mouse_pos)
        if clicked_block_and_bombs_near:
            clicked_block, bombs_near_block = clicked_block_and_bombs_near
            self.open_zero_blocks(clicked_block, bombs_near_block)
            clicked_block.react_on_click(mouse_keys, bombs_near_block)
            # self.calculate_count_of_marked_blocks()

        # if bombs_near_block == 0:
        #     clicked_block.



    def update(self, mouse_keys, mouse_pos):
        self.update_blocks(mouse_keys, mouse_pos)
        self.check_bombs_state()

        if self.a:
            return self.a

            # self.block.change_image(image)
        # if self.check_mouse_click_on_blocks(mouse_keys, mouse_pos):
