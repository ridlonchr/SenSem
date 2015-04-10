from soldier import *
import pygame

#initialize pygame
pygame.init()

"""
class Game(object):

    def __init__(self):

        self.playes = raw_input("How many people are playing? ")
        player_list = Soilder_container()

        for player in range(int(self.player_count)):
            player_list.add_to_dict()
"""
def __init__(self, text="text", font="calibri", font_size=30,
                 font_color=(0, 0, 0), (pos_x, pos_y)=(0, 0)):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

class GameMenu(object):

    def __init__(self):

        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.background =  pygame.image.load('bg.png')
        self.background_rect = self.background.get_rect()

        self.clock = pygame.time.Clock()

        self.menu_items = ('New Game', 'Quit')

        self.font = pygame.font.SysFont("calibri", 22, True)
        self.font_color = (0,0,0)

        self.menu_items = []
        for index, item in enumerate(('New Game', 'Quit')):
            label = self.font.render(item, 1, self.font_color)

            width = label.get_rect().width
            height = label.get_rect().height

            posx = (self.screen_width / 2) - (width / 2)

            total_height_text = len(self.menu_items) * height
            posy = ((self.screen_height / 2) + (total_height_text / 2) + (index * height)-80)

            self.menu_items.append([item, label, (width, height), (posx, posy)])
    def run(self):
        mainloop = True
        while mainloop:
            #limit fps to fitty
            self.clock.tick(50)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False

            #redraw bg
            self.screen.blit(self.background, self.background_rect)

            for name, label, (width, height), (posx, posy) in self.menu_items:
                self.screen.blit(label, (posx, posy))

            pygame.display.flip()

"""
test
"""

pygame.display.set_caption('Infinite War')
gm = GameMenu()
gm.run()
