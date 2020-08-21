import pygame


class Block:
    def __init__(self, screen: pygame.display, pos: tuple, size: int):
        self.screen = screen
        self.pos = pos
        self.size = size
        self.image = pygame.Surface((self.size - 3, self.size - 3))
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, (255, 255, 255), self.rect)
        self.rect.topleft = self.pos
        # self.rect = pygame.Rect(*pos, size - 2, size - 2)
        # self.color = (255, 255, 255)
        self.is_open = False
        self.is_bomb = False
        self.is_marked = False
        # self.bombs_near = 0



    def draw(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.pos)

    def change_image(self, image):
        self.image.fill((255, 255, 255))
        self.image.blit(image, (self.size // 4, 0))

    def react_on_click(self, mouse_keys, bombs_near):
        font = pygame.font.Font(pygame.font.match_font('arial'), 40)

        if mouse_keys[0] and not self.is_open and not self.is_marked:
            if self.is_bomb:
                self.is_open = True
                image = font.render('*', True, (255, 0, 0))
                self.change_image(image)
                # print('BOMB')
            elif not self.is_marked:
                self.is_open = True
                image = font.render(str(bombs_near), True, (0, 0, 255))
                self.change_image(image)


        elif mouse_keys[2] and not self.is_open:
            if not self.is_marked:
                self.is_marked = True
                image = font.render('|>', True, (0, 255, 0))
                self.change_image(image)
            elif self.is_marked:
                self.is_marked = False
                self.image.fill((255, 255, 255))

            # else:
            #     self.image.fill((255, 255, 255))
                # self.is_marked = False





    # def mouse_click(self, mouse):
    #     rect = self.image.get_rect()
    #     self.image.fill((255, 255, 255))
    #     if mouse[0]:
    #         if self.is_bomb:
    #             font = pygame.font.Font(pygame.font.match_font('arial'), 50)
    #             image = font.render('*', True, (255, 0, 0))
    #             self.image.blit(image, (self.size // 4, 0))
    #             print('bomb')
    #             # pygame.draw.rect(self.image, (255, 0, 0), rect)
    #         else:
    #             font = pygame.font.Font(pygame.font.match_font('arial'), 50)
    #             image = font.render(str(self.bombs_near), True, (0, 0, 255))
    #             self.image.blit(image, (self.size // 4, 0))
    #
    #     elif mouse[2]:
    #         font = pygame.font.Font(pygame.font.match_font('arial'), 50)
    #         image = font.render('|>', True, (0, 255, 0))
    #         self.image.blit(image, (self.size // 4, 0))

            # self.image.fill((0, 0, 255))
        # self.color = (0, 255, 0)
        # self.
        # pygame.draw.rect(self.image, (0, 255, 0), rect)



    # def
