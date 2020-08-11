import pygame
from figure import Figure


# from settings import *


class App:
    def __init__(self):
        # self.running = True
        self.block_size = 50
        self.block_count = (10, 15)
        self.res = (self.block_count[0] * self.block_size, self.block_count[1] * self.block_size)
        self.decor_grid = [pygame.Rect(x * self.block_size, y * self.block_size, self.block_size, self.block_size) for x
                           in range(self.block_count[0])
                           for y in range(self.block_count[1])]

        self.figures_grid = [[0 for x in range(self.block_count[0] + 2)] for y in range(self.block_count[1])]

        self.screen = pygame.display.set_mode(self.res)
        self.figure = Figure(self.screen, self.block_size, self.block_count, self.figures_grid)
        self.keys = None
        self.clock = pygame.time.Clock()
        pygame.init()
        # [pygame.draw.rect(self.screen, (255, 255, 255), block, 1) for block in self.grid]
        # self.figure.draw()
        # pygame.display.flip()

    # figure1 = [[(-1, -1), (-2, -1), (0, -1), (1, -1)]]
    # figure1 = [[(0, -1), (0, -2), (1, -2), (0, 0)]]

    # def move():
    #     for i in range(4):
    #         figure2[i].y += 1

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                self.keys = pygame.key.get_pressed()

    def update(self, dt):
        self.figure.update(self.keys, dt)
        # self.figure.update(self.keys)
        # self.figure.figure[0].y += 1
        # a = deepcopy(self.figure)
        # self.figure.update(self.keys)
        # self.figure.move()
        # self.figure.move()
        # self.figure.check_borders()
        # self.figure.move_with_check_borders()

    # if figure2[0].y * self.block_size >= blocks_count[1] * block_size:
    #     figure2 = a

    def render(self):
        self.screen.fill(pygame.Color('black'))
        [pygame.draw.rect(self.screen, (255, 255, 255), block, 1) for block in self.decor_grid]
        self.figure.draw()
        self.draw_finished_figures()

        pygame.display.flip()

    def draw_finished_figures(self):
        for y, row in enumerate(self.figures_grid):
            for x, column in enumerate(row):
                if column:
                    # pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x, y, 50, 50), 50)
                    # self.rect.x = self.figure[i].x * self.block_size
                    # self.rect.y = self.figure[i].y * self.block_size
                    self.figure.rect.x, self.figure.rect.y = x * self.block_size, y * self.block_size
                    pygame.draw.rect(self.screen, (255, 255, 255), self.figure.rect)

    def run(self):
        self.keys = pygame.key.get_pressed()
        while True:
            dt = self.clock.tick(5)
            # print(dt)
            self.event_loop()
            self.update(dt)
            self.render()

        # while True:
        #
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             exit()


if __name__ == '__main__':
    app = App()
    app.run()
