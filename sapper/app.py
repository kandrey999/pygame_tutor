import pygame
from grid import Grid


# pygame.Rect()
class App:
    def __init__(self, block_size: int, block_count: tuple, bombs_count: int):
        pygame.init()
        self.block_size = block_size
        self.block_count = block_count
        self.bombs_count = bombs_count
        self.res = self.block_size * self.block_count[0], self.block_size * self.block_count[1]
        # self.mouse_keys = pygame.mouse.get_pressed()
        self.last_mouse_pos = pygame.mouse.get_pos()
        self.mouse_keys = (0, 0, 0)
        # self.res = self.block_size * self.block_count[0], self.block_size * self.block_count[1]
        self.screen = pygame.display.set_mode(self.res)
        self.grid = Grid(self.screen, self.block_size, self.block_count, self.bombs_count)
        self.clock = pygame.time.Clock()
        self.game = True
        # self.check()
        # [[print(block.is_bomb) for block in row] for row in self.grid.grid]
        # self.decor_grid = [pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size) for x in range(self.block_count[0]) for y in range(self.block_count[1])]
        # self.grid = [[0 for x in range(self.block_count[0])] for y in range(self.block_count[1])]
        # self. grid = [[Block(self.screen, (x * self.block_size, y * self.block_size), self.block_size) for x in range(self.block_count[0])] for y in range(self.block_count[1])]


    def event_loop(self):
        self.mouse_keys = (0, 0, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('EXIT')
                exit()
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                self.mouse_keys = pygame.mouse.get_pressed()
                self.last_mouse_pos = pygame.mouse.get_pos()

            # self.grid.check_mouse_click(pygame.mouse.get_pos(), mouse)
            # print('press')
        # elif pygame.mouse.get_pressed()[1]:

    def update(self):
        # print(self.mouse_keys, self.last_mouse_pos)
        a = self.grid.update(self.mouse_keys, self.last_mouse_pos)
        if a:
            self.game = False

    def render(self):
        self.screen.fill(pygame.Color('black'))
        self.grid.draw()
        pygame.display.flip()
        # pygame.draw.rect(self.screen, pygame.Color('white'), pygame.Rect(10, 10, 50, 50), 10)
        # [pygame.draw.rect(self.screen, pygame.Color('black'), block, 2) for block in self.decor_grid]
        # [[block.draw() for block in row] for row in self.grid]

    def run(self):
        while True:
            self.clock.tick(60)
            self.event_loop()
            if self.game:
                self.update()
            self.render()
            # print(self.fps)
            # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(100, 100, 50, 50), 10)
            # (pygame.draw.rect(self.screen, (255, 255, 255), block, 2) for block in self.decor_grid)


if __name__ == '__main__':
    app = App(50, (10, 10), 10)
    app.run()

# app = App(50, (10, 10), 2, 60)
# app.run()
