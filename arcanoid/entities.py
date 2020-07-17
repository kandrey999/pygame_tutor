import math
import pygame as pg
from random import randrange, random


class Player:
    def __init__(self, width: int, height: int, speed: int, area: pg.Rect):
        self.image = pg.Surface((width, height))
        self.rect = self.image.get_rect(midbottom=(area.width // 2, area.height - 10))
        self._speed = speed
        self._area = area
        self.draw()

    def update(self, keys, dt):
        if keys[pg.K_LEFT]:
            self.move(-self._speed * dt)
        elif keys[pg.K_RIGHT]:
            self.move(self._speed * dt)

    def move(self, distance):
        self.rect.left = min(max(self.rect.left + distance, 0), self._area.right - self.rect.width)

    def draw(self):
        pg.draw.rect(self.image, pg.Color('red'), self.image.get_rect())


class Ball:
    def __init__(self, radius: int, speed: int, area: pg.Rect):
        self.radius = radius
        self.speed = speed
        self.area = area
        self.image = pg.Surface((radius * 2, radius * 2))
        self.image.set_colorkey(pg.Color('black'))
        self.rect = self.image.get_rect(center=area.center)
        self.pos = area.center
        self._rotation = (random() - 0.5) * (math.pi / 2) - (math.pi / 2)
        self.draw()

    def update(self, dt):
        distance = dt * self.speed
        self.move(distance)
        self.check_borders()

    def move(self, distance):
        dx = distance * math.cos(self._rotation)
        dy = distance * math.sin(self._rotation)
        self.pos = self.pos[0] + dx, self.pos[1] + dy
        self.rect.center = self.pos

    @staticmethod
    def get_epsilon():
        epsilon = (random() - 0.5) * math.pi / 15
        return epsilon

    def check_borders(self):
        if self.rect.centerx < self.radius or self.rect.centerx > self.area.width - self.radius:
            self._rotation = math.pi - self._rotation + self.get_epsilon()
        elif self.rect.centery < self.radius:
            self._rotation = -self._rotation + self.get_epsilon()

    def check_collide_with_player(self, player):
        if self.rect.colliderect(player) and math.sin(self._rotation) > 0:
            self._rotation = -self._rotation + self.get_epsilon()

    def check_collide_with_bricks(self, bricks):
        for i, brick in enumerate(bricks):
            if self.rect.colliderect(brick.rect):
                self.check_collide_side(bricks.pop(i))

    def check_collide_side(self, brick):
        if 0 <= self._rotation <= math.pi:
            delta_y = self.rect.bottom - brick.rect.top
        else:
            delta_y = brick.rect.bottom - self.rect.top

        if -math.pi / 2 <= self._rotation <= math.pi / 2:
            delta_x = self.rect.right - brick.rect.left
        else:
            delta_x = brick.rect.right - self.rect.left

        if delta_x > delta_y:
            self._rotation = -self._rotation + self.get_epsilon()
        else:
            self._rotation = math.pi - self._rotation + self.get_epsilon()

    def draw(self):
        pg.draw.circle(self.image, pg.Color('green'), self.image.get_rect().center, self.radius)


class Brick:
    def __init__(self, pos: tuple, size: tuple, color: pg.Color = None):
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect(topleft=pos)
        self._color = color or pg.Color(randrange(16, 240), randrange(16, 240), randrange(16, 240))

        self.draw()
        # self._pos = pos

    def draw(self):
        pg.draw.rect(self.image, self._color, self.image.get_rect())
