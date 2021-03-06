import os
import pygame as pg


class App:
    def __init__(self):
        self.size = self.width, self.height = 1200, 800
        self.screen = pg.display.set_mode(self.size)
        self.rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.keys = pg.key.get_pressed()

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type in (pg.KEYUP, pg.KEYDOWN):
                self.keys = pg.key.get_pressed()

    def update(self, dt):
        pass

    def render(self):
        self.screen.fill(pg.Color('black'))
        pg.display.flip()

    def display_fps(self):
        caption = f'FPS: {self.clock.get_fps():.2f}'
        pg.display.set_caption(caption)

    def run(self):
        while True:
            dt = self.clock.tick(100) / 1000
            self.event_loop()
            self.update(dt)
            self.render()
            self.display_fps()


if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    app = App()
    app.run()
