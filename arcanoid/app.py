import os
import pygame as pg
from entities import *
from random import choice, randrange


class App:
    def __init__(self):
        self.size = self.width, self.height = 1200, 800
        self.screen = pg.display.set_mode(self.size)
        self.rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()
        self.player = Player(100, 20, 500, self.rect)
        self.ball = Ball(20, 450, self.rect)
        self.brick_colors = ['red', 'yellow', 'green', 'orange', 'purple']
        self.bricks = [Brick((10 + 70 * i, 10 + 40 * j), (50, 20)) for i in range(17) for j in range(5)]
        # self.brick = Brick((50, 20), (100, 100), pg.Color('yellow'))

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys = pg.key.get_pressed()

    def update(self, dt):
        self.player.update(self.keys, dt)
        self.ball.update(dt)
        self.ball.check_collide_with_player(self.player)
        self.ball.check_collide_with_bricks(self.bricks)

    def render(self):
        self.screen.fill(pg.Color('darkblue'))
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.ball.image, self.ball.rect)
        [self.screen.blit(brick.image, brick.rect) for brick in self.bricks]
        # self.screen.blit(self.brick.image, self.brick.rect)
        pg.display.flip()

    def display_fps(self):
        caption = f'FPS: {self.clock.get_fps():.2f}'
        pg.display.set_caption(caption)

    def run(self):
        while True:
            dt = self.clock.tick(300) / 1000
            self.event_loop()
            self.update(dt)
            self.render()
            self.display_fps()


if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    app = App()
    app.run()
