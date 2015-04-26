# stardard inputs that i need
import sys, os, pygame
# this is a module written by: David Clark
# i use this class to render text rectangle if you will
#web = http://www.pygame.org/pcr/text_rect/index.php
from textWrapper import *

from pygame.locals import *

# class i created
import soldier

# class i created
import soilder1

# class i created
import d20

pygame.mixer.pre_init(44100, -16, 2, 2048)
#initialize pygame
pygame.init()

"""
General Menu Item Text Class
Derived from pygames Font class

Allows me to take a string and put it on the screen
text created can be used as a button
"""
class MenuItem(pygame.font.Font):
    def __init__(self, text="text", font=None, font_size=30,
                 font_color=(0, 0, 0), (pos_x, pos_y)=(0, 0),):
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.is_selected = False
        self.button_rect = pygame.Rect(pos_x,pos_y,self.width+6,self.height+2 )
        self.button_surface = pygame.Surface(self.button_rect.size)

    # sets the text coordinates
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    """
    pygame rect is a set of rectangular coordinates
    aka draws a rectangle with the given coordinates
    """
    def set_rect(self, x, y):
        self.button_rect = pygame.Rect(x,y,self.width+6,self.height+2 )


    # takes a color and  changes it to that color
    def set_font_color(self, color):
        self.font_color = color
        self.label = self.render(self.text, 1, self.font_color)

    """
    determines if the mouse is currently hovering over the selection,
    returns a boolean depending on if the mouse is or not
    """
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        # else returns false
        return False

"""
Game Screen is the general framework for screen creation
this allows me to create multiple differnt screens and backgrounds
"""
class GameScreen(object):

    def __init__(self,background='pic/bg.png',music="sound/menu_song.wav", funcs={}):
    # initialize the screen
        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.background =  pygame.image.load(background)
        self.background_rect = self.background.get_rect()

        self.funcs = funcs
        self.playerName = ''
        self.clock = pygame.time.Clock()

        # init music
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1, 0.0)

        self.is_running = False


    # if the user uses the keyboard the mouse will disapear this checks if it should be or not
    def toggle_mouse_visibility(self):
        if self.mouse_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)

    # highlights the menu item that the mouse is hovering over
    def toggle_text_mouseover(self, item, mouse_position, font_color1=(255, 255, 255), font_color2=(0, 0, 0)):
        if item.is_mouse_selection(mouse_position):
            item.set_font_color(font_color1)
            item.set_bold(True)
            #else it is just normal
        else:
            item.set_font_color(font_color2)
            item.set_bold(False)

    def set_keyboard_selection(self,key):
        # highlights the menu item chosen with the keyboard
        for item in self.menu_items:
            # set the font and bold to defaul values
            item.set_bold(False)
            item.set_font_color((0, 0, 0))

        if self.cur_item is None:
            self.cur_item = 0
        else:
            # find the item selected
            # moves the selection up one
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            # if the top item is selected then choose the last item
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.menu_items) - 1
            # move the item down one
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.menu_items) - 1:
                self.cur_item += 1
            # if the bottom item is selected then choose the first item
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.menu_items) - 1:
                self.cur_item = 0
            # check to see if enter was pushed
        if key == pygame.K_RETURN:
            text = self.menu_items[self.cur_item].text
            # terminate the mainloop so we do not have several loops running at one time
            self.is_running = False
            # call the corresponding function
            if text == 'Quit':
                self.funcs[text]()
            else:
                self.funcs[text](self)

        #highlights the appropiate item
        self.menu_items[self.cur_item].set_bold(True)
        self.menu_items[self.cur_item].set_font_color((255, 255, 255))

    def stop_music(self):
        pygame.mixer.music.stop()


class GameMenu(GameScreen):

    def __init__(self):

        # create mt menu items
        my_items = ('New Game', 'High Score' ,'Quit')

        # dict of functions that will hook up to my functions
        self.funcs = {'New Game': new_game,
                      'High Score' : high_score,
                      'Quit': sys.exit}

        GameScreen.__init__(self,'pic/bg.png',"sound/menu_song.wav",self.funcs)

        self.menu_items = []
        for index, item in enumerate(my_items):
            #initialize a menu item
            menu_item = MenuItem(item)

            #get coordinates for the buttons
            posx = (self.screen_width / 2) - (menu_item.width / 2)
            posy = ((self.screen_height / 2) +  ((index * 3) + index * menu_item.height) + 50)

            #add the menu_item to the GameMenu
            menu_item.set_position(posx, posy)
            menu_item.set_rect(posx-3, posy-2)
            self.menu_items.append(menu_item)

        self.mouse_visible = True
        self.cur_item = None
        self.nextscreen = 0

    def run(self):
        self.is_running = True
        while self.is_running:

            #limit fps to fitty
            self.clock.tick(50)

            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.mouse_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.menu_items:
                        if item.is_mouse_selection(mouse_position):
                            if item.text == 'Quit':
                                self.funcs[item.text]()
                                self.is_running = False
                            if item.text == 'Back':
                                return

                            else:
                                self.funcs[item.text](self)
                                self.is_running = False

            # checks to see if the mouse has moved, shows the cursur again if it was off
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_visible = True
                self.cur_item = None

            self.toggle_mouse_visibility()

            #redraw bg
            self.screen.blit(self.background, self.background_rect)

            #draw the items and check for a mouseover if the mouse is visible
            for item in self.menu_items:
                if self.mouse_visible:
                    self.toggle_text_mouseover(item, mouse_position)
                self.screen.blit(item.label, item.position)

            pygame.display.flip()

class HighScoreScreen(GameScreen):

    def __init__(self):
        # create my menu items
        my_items = ('Back', '')

        self.funcs = {'Back': back,
                    '' : back}


        GameScreen.__init__(self,'pic/highscores.png',"sound/menu_song.wav",self.funcs)

        self.score_handler =  HighScore_Handler()

        self.menu_items = []
        for index, item in enumerate(my_items):
            #initialize a menu item
            menu_item = MenuItem(item)

            #get coordinates for the buttons
            posx = ((640 / 2) - (menu_item.width / 2))
            posy = 430

            #add the menu_item to the GameMenu
            menu_item.set_position(posx, posy)
            menu_item.set_rect(posx-3, posy-2)
            self.menu_items.append(menu_item)


        self.mouse_visible = True
        self.cur_item = None
        self.nextscreen = 0

    def run(self):
        self.is_running = True
        while self.is_running:

            #limit fps to fitty
            self.clock.tick(50)

            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.menu_items:
                        if item.is_mouse_selection(mouse_position):
                            if item.text == 'Back':
                                self.is_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.is_running = False
                    self.mouse_visible = False
                    self.cur_item = 0
                    self.menu_items[self.cur_item].set_bold(True)
                    self.menu_items[self.cur_item].set_font_color((255, 255, 255))


            # checks to see if the mouse has moved, shows the cursur again if it was off
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_visible = True
                self.cur_item = None

            self.toggle_mouse_visibility()

            #redraw bg
            self.screen.blit(self.background, self.background_rect)

            #draw the items and check for a mouseover if the mouse is visible
            for item in self.menu_items:
                if self.mouse_visible:
                    self.toggle_text_mouseover(item, mouse_position,(255,255,255),(255,255,255))
                self.screen.blit(item.label, item.position)
            #draw the highscores and blit them to the screen
            for score in self.score_handler.score_list:
                score.set_font_color((255,255,255))
                self.screen.blit(score.label, score.position)

            pygame.display.flip()





"""
This Class generates the loading screen, i do not know
if i need to use this or not, regardless here is the code

work to do:
fix the def run to work properly
add something like a loading bar, dial etc...
"""
class LoadingScreen(GameScreen):

    def __init__(self, background):
            self.Game_Screen = GameScreen(background)
            self.ls_bg = background


            pygame.display.flip()

    def run(self):
        self.is_running = True
        while self.is_running:
            #limit fps to fitty
            self.Game_Screen.clock.tick(50)
            self.Game_Screen.redraw(self.ls_bg)
            pygame.display.flip()

class NewGameScreen(GameScreen):
    def __init__(self):
        self.playerName = ''
        my_items = ('Continue', '')

        self.funcs = {'Continue': move_on,'' : move_on}
        GameScreen.__init__(self,'pic/newgamescreen.png',"sound/menu_song.wav",self.funcs)
        self.menu_items = []
        for index, item in enumerate(my_items):
            #initialize a menu item
            menu_item = MenuItem(item)

            #get coordinates for the buttons
            posx = 540 - (90/2)
            posy = 430

            #add the menu_item to the GameMenu
            menu_item.set_position(posx, posy)
            menu_item.set_rect(posx-3, posy-2)
            self.menu_items.append(menu_item)
        self.mouse_visible = True
        self.cur_item = None
        self.nextscreen = 0


    def get_name(self,font):
        name = ''
        while True:
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name += evt.unicode
                    elif evt.key == K_BACKSPACE:
                        name = name[:-1]
                    elif evt.key == K_RETURN:
                        return name

                elif evt.type == QUIT:
                    return
            block = font.render(name, True, (255, 255, 255))
            rect = pygame.Rect((480,230,172,480))
            self.screen.blit(block, rect)
            pygame.display.flip()

    def run(self):
        self.is_running = True
        my_font = pygame.font.Font('font/gunplayrg.ttf', 18)
        my_rect = pygame.Rect((464, 30, 172, 480))
        my_returnrect = pygame.Rect((pygame.Rect((464, 260, 172, 480))))
        while self.is_running:

            #limit fps to fitty
            self.clock.tick(50)

            mouse_position = pygame.mouse.get_pos()
            events = pygame.event.get()

            for event in events:
                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.menu_items:
                        if item.is_mouse_selection(mouse_position):
                            if item.text == 'Continue':
                                self.funcs[item.text](self.playerName, self)
                                self.is_running = False

                if event.type == pygame.KEYDOWN and self.playerName == '':
                    self.playerName = self.get_name(my_font)
            if self.playerName != '':

                my_string = "So your name is " + self.playerName + ". You better make me proud private"
                rendered_text = render_textrect(my_string, my_font, my_rect, (255, 255, 255), 1)
                if rendered_text:
                    self.screen.blit(rendered_text, my_returnrect)
            pygame.display.update(my_returnrect)
            self.screen.blit(self.background, self.background_rect)


            # checks to see if the mouse has moved, shows the cursur again if it was off
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_visible = True
                self.cur_item = None

            self.toggle_mouse_visibility()

            #redraw bg
            self.screen.blit(self.background, self.background_rect)

            #draw the items and check for a mouseover if the mouse is visible
            for item in self.menu_items:
                if self.mouse_visible:
                    self.toggle_text_mouseover(item, mouse_position,(0,0,0),(255,255,255))
                self.screen.blit(item.label, item.position)


            my_string = "Colonel Major: Welcome to the battlefield, \n we need fresh recruits... \n Whats your name soldier?"
            rendered_text = render_textrect(my_string, my_font, my_rect, (255, 255, 255), 1)

            if rendered_text:
                self.screen.blit(rendered_text, my_rect)
            #pygame.display.flip()


            pygame.display.flip()

class TheGameScreen(GameScreen):
    def __init__(self):
        # create mt menu items
        soldier1 = ('Attack', 'Melee' ,'Reload')
        soldier2 = ('Attack', 'Heal' ,'Reload')
        soldier3 = ('Attack', 'Snipe' ,'Reload')

        my_items = soldier1 + soldier2 + soldier3
        # dict of functions that will hook up to my functions
        self.funcs = {'Attack': attack,
                      'Melee' : melee,
                      'Reload': reload_wep,
                      'Heal'  : heal,
                      'Snipe' : snipe}

        GameScreen.__init__(self,'pic/gamebg.png',"sound/menu_song.wav",self.funcs)

        self.menu_items = []
        for index, item in enumerate(my_items):
            #initialize a menu item
            menu_item = MenuItem(item)

            if len(self.menu_items) <=2:
                #get coordinates for the buttons
                posx = (self.screen_width / 2) - (menu_item.width / 2)
                posy = ((300) +  ((index * 3) + index * menu_item.height) + 50)

                #add the menu_item to the GameMenu
                menu_item.set_position(posx, posy)
                menu_item.set_rect(posx-3, posy-2)
                self.menu_items.append(menu_item)
            elif len(self.menu_items) <=5 and len(self.menu_items) > 2:
                #get coordinates for the buttons
                posx = ((self.screen_width / 2) - (menu_item.width / 2)+70)
                posy = ((300) +  ((index * 3) + index * menu_item.height) + 50)

                #add the menu_item to the GameMenu
                menu_item.set_position(posx, posy)
                menu_item.set_rect(posx-3, posy-2)
                self.menu_items.append(menu_item)
            elif len(self.menu_items) <=8 and len(self.menu_items) > 5:
                #get coordinates for the buttons
                posx = ((self.screen_width / 2) - (menu_item.width / 2)+140)
                posy = ((300) +  ((index * 3) + index * menu_item.height) + 50)

                #add the menu_item to the GameMenu
                menu_item.set_position(posx, posy)
                menu_item.set_rect(posx-3, posy-2)
                self.menu_items.append(menu_item)

        self.mouse_visible = True
        self.cur_item = None
        self.nextscreen = 0

    def run(self):
        self.is_running = True
        while self.is_running:

            #limit fps to fitty
            self.clock.tick(50)

            mouse_position = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.mouse_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.menu_items:
                        if item.is_mouse_selection(mouse_position):
                            if item.text == 'Quit':
                                self.funcs[item.text]()
                                self.is_running = False
                            if item.text == 'Back':
                                return

                            else:
                                self.funcs[item.text](self)
                                self.is_running = False

            # checks to see if the mouse has moved, shows the cursur again if it was off
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_visible = True
                self.cur_item = None

            self.toggle_mouse_visibility()

            #redraw bg
            self.screen.blit(self.background, self.background_rect)

            #draw the items and check for a mouseover if the mouse is visible
            for item in self.menu_items:
                if self.mouse_visible:
                    self.toggle_text_mouseover(item, mouse_position)
                self.screen.blit(item.label, item.position)

            pygame.display.flip()

"""
This Class generates the high scores page
Its rudimentary, but i use a text file to store the highscores

work to do:
be able to update and keep track of current high scores.
"""
class HighScore_Handler(object):

    def __init__(self, textfile='highScores.txt'):
        self.source_file = file(textfile)
        self.highScores_dict = {}
        self.score_list = []
        # read through the file
        linenum = 0
        while linenum < 10:
            line = self.source_file.readline()
            # break if end of file
            if not line: break
            linelist = line.split()
            self.highScores_dict[linelist[1]] = int(linelist[2])
            linenum+=1

        self.source_file.close()
        # a list of sorted dictionary key and values
        self.highScores_dict = sorted([(value,key) for (key,value) in self.highScores_dict.items()])

        posy = 420
        increment = 30
        for key in self.highScores_dict:
            stringScore = self.key_to_string(key)
            menu_item = MenuItem(stringScore)
            #get coordinates for the buttons
            posx = ((480 / 2) - (menu_item.width / 2)+90)
            posy -= increment
            menu_item.set_position(posx, posy)
            self.score_list.append(menu_item)


    def key_to_string(self, key):
        string = str(key[1]) + ' ' +str(key[0])
        return string

    # test function
    def print_dict(self):
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.highScores_dict)



"""
Globally Define Functions
Used to handle switching screens
_______________________________________________
this function is linked to the button High Score
changes the nextscreen variable to 2, signifying
that the game should switch to the high score screen
______________________________________________
"""

def high_score(old_screen):
    old_screen.nextscreen = 2

"""
_______________________________________________
this function is linked to the button new game
changes the nextscreen variable to 1, signifying
that the game should begin a new game
______________________________________________
"""
def new_game(old_screen):
    old_screen.nextscreen = 1

def move_on(name,old_screen):
    old_screen.playerName = name
    old_screen.nextscreen = 3

def back(old_screen):
    old_screen.nextscreen = 0
def attack():
    pass
def reload_wep():
    pass
def melee():
    pass
def snipe():
    pass
def heal():
    pass

# tests
if __name__ == '__main__':
    pygame.display.set_caption('Infinite War')
    gm = GameMenu()
    ngs = NewGameScreen()
    hs = HighScoreScreen()
    tgs = TheGameScreen()
    while True:
        gm.run()
        if gm.nextscreen == 1:
            ngs.run()
            if ngs.nextscreen == 3:
                print "yo bitch"
                tgs.run()
                print "i aint no bitch"
        elif gm.nextscreen == 0:
            gm.run()
        elif gm.nextscreen == 2:
            hs.run()
        else:
            sys.exit()
