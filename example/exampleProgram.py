import pygame
from pygame.locals import *

def name(self,font):
    name =''
    while True:
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                if evt.unicode.isalpha():
                    self.name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    self.name = self.name[:-1]
                elif evt.key == K_RETURN:
                    return name
            elif evt.type == QUIT:
                return
        block = font.render(name, True, (255, 255, 255))
        rect = block.get_rect()
        rect.center = screen.get_rect().center
        screen.blit(block, rect)
        pygame.display.flip()

if __name__ == "__main__":
    name()
