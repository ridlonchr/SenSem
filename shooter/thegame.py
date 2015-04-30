from game_class import *
from soldier import *

class TheGameScreen(GameScreen):
    def __init__(self,playername):

        self.player_name = str(playername)

        # create mt menu items
        soldier1 = ('Attack1', 'Melee' ,'Reload1')
        soldier2 = ('Attack2', 'Heal' ,'Reload2')
        soldier3 = ('Attack3', 'Snipe' ,'Reload3')

        my_items = soldier1 + soldier2 + soldier3
        # dict of functions that will hook up to my functions
        self.funcs = {'Attack1': self.attack1,
                      'Attack2': self.attack2,
                      'Attack3': self.attack3,
                      'Melee'  : self.melee,
                      'Reload1': self.reload1,
                      'Reload2': self.reload2,
                      'Reload3': self.reload3,
                      'Heal'   : self.heal,
                      'Snipe'  : self.snipe}

        self.my_rect = pygame.Rect((431, 331, 200, 140))
        self.my_font = pygame.font.Font(None, 18)
        self.my_text = ""
        self.textlines = 0

        self.my_rectinfan =  pygame.Rect((23,350,150,150))
        self.my_rectmedic =  pygame.Rect((148,350,150,150))
        self.my_rectsniper =  pygame.Rect((273,350,150,150))

        #initalize your team
        self.container = Soldier_container()

        self.infantry = Infantry("Infantry Joe")
        self.container.add_to_dict(self.infantry)

        self.medic = Medic("Medic Francisco")
        self.container.add_to_dict(self.medic)

        self.sniper = Sniper("Sniper Charlie")
        self.container.add_to_dict(self.sniper)

        # init enemy
        self.enemy_container = Soldier_container()
        self.enemy = Infantry("Commy")


        GameScreen.__init__(self,'pic/gamebg.png',"sound/menu_song.wav",self.funcs)




        self.menu_items = []
        for index, item in enumerate(my_items):
            menu_item = MenuItem(item)

            if len(self.menu_items) <=2:
                #get coordinates for the buttons
                posy = 407 + (index*25)
                posx = (menu_item.height)


                #add the menu_item to the GameMenu
                menu_item.set_position(posx, posy)
                menu_item.set_rect(posx-3, posy-2)
                self.menu_items.append(menu_item)

            elif len(self.menu_items) <=5 and len(self.menu_items) > 2:
                #get coordinates for the buttons
                posy = 407 + ((index-3)*25)
                posx = (125 +  menu_item.height)

                #add the menu_item to the GameMenu
                menu_item.set_position(posx, posy)
                menu_item.set_rect(posx-3, posy-2)
                self.menu_items.append(menu_item)

            elif len(self.menu_items) <=8 and len(self.menu_items) > 5:
                #get coordinates for the buttons
                posy = 407 + ((index-6)*25)
                posx = (250 + menu_item.height)
                #posy = (350 + menu_item.height)

                #add the menu_item to the GameMenu
                menu_item.set_position(posx, posy)
                menu_item.set_rect(posx-3, posy-2)
                self.menu_items.append(menu_item)

        self.mouse_visible = True
        self.cur_item = None
        self.nextscreen = 0

    def text_string(self,string):
        self.textlines += 1
        if self.textlines <= 9:
            self.my_text += str(string)
        else:
            self.textlines = 0
            self.my_text = str(string)


    def init_textbox(self):
        rendered_text = render_textrect_color(self.my_text, self.my_font, self.my_rect, (255,255,255) ,(0,0,0), 0)
        self.screen.blit(rendered_text,self.my_rect.topleft)

    def display_labels(self):
        # put the titles to the buttons
        my_string = self.infantry.name + "\nHP: " + str(self.infantry.hitpoints) +"\nArmor: " + str(self.infantry.armor) + "\nAmmo: " + str(self.infantry.ammo)
        rendered_text = render_textrect(my_string, self.my_font, self.my_rectinfan, (255, 255, 255), 0)

        if rendered_text:
            self.screen.blit(rendered_text, self.my_rectinfan)

        my_string = self.medic.name + "\nHP: " + str(self.medic.hitpoints) +"\nArmor: " + str(self.medic.armor) + "\nAmmo: " + str(self.medic.ammo)
        rendered_text = render_textrect(my_string, self.my_font, self.my_rectmedic, (255, 255, 255), 0)

        if rendered_text:
            self.screen.blit(rendered_text, self.my_rectmedic)

        my_string = self.sniper.name + "\nHP: " + str(self.sniper.hitpoints) +"\nArmor: " + str(self.sniper.armor) + "\nAmmo: " + str(self.sniper.ammo)
        rendered_text = render_textrect(my_string, self.my_font, self.my_rectsniper, (255, 255, 255), 0)

        if rendered_text:
            self.screen.blit(rendered_text, self.my_rectsniper)

    def display_name(self):
        my_font = pygame.font.Font(None, 22)
        my_rect = pygame.Rect((23,330,150,150))
        my_string = "Player:" + self.player_name
        rendered_text = render_textrect(my_string, my_font, my_rect, (255, 255, 255), 0)

        if rendered_text:
            self.screen.blit(rendered_text, my_rect)

    def attack1(self, infantry, enemy):
        d20 =  d20_Combat(infantry,enemy)
        infantry.ammo -= 1
        if d20.damage == -1:
            self.text_string("\nThe Enemy dodged your attack!")
        elif d20.damage == 0:
            self.text_string("\nYou Missed!")
        elif d20.damage > 0:
            self.text_string("\nHit! You did " + str(d20.damage) + " damage!")
            enemy.hitpoints = enemy.hitpoints - d20.damage



    def attack2(self, medic):
        d20 =  d20_Combat(medic,enemy)
        medic.ammo -= 1
        if d20.damage== -1:
            self.text_string("\nThe Enemy dodged your attack!")
        elif d20.damage == 0:
            self.text_string("\nYou Missed!")
        elif d20.damage > 0:
            self.text_string("\nHit! You did " + str(damage) + " damage!")
            enemy.hitpoints = enemy.hitpoints - d20.damage

    def attack3(self, sniper):
        d20 =  d20_Combat(sniper,enemy)
        sniper.ammo -= 1
        if d20.damage == -1:
            self.text_string("\nThe Enemy dodged your punch!")
        elif d20.damage == 0:
            self.text_string("\nYou Missed...bro...")
        elif d20.damage > 0:
            self.text_string("\nHit! You did " + str(damage) + " damage!")
            enemy.hitpoints = enemy.hitpoints - d20.damage

    def reload1(self,infantry):
        infantry.ammo = 15
        self.text_string("\nInfantry reloaded")

    def reload2(self,medic):
        infantry.ammo = 10
        self.text_string("\nMedic reloaded")

    def reload3(self,sniper):
        infantry.ammo = 7
        self.text_string("\nSniper reloaded")

    def melee(self, infantry, enemy):
        d20 =  d20_Combat(infantry,enemy)
        # melee penalty
        damage = d20.damage - 2
        if damage == -1:
            self.text_string("\nThe Enemy dodged your punch!")
        elif damage == 0:
            self.text_string("\nYou Missed...bro...")
        elif damage > 0:
            self.text_string("\nHit! You did " + str(damage) + " damage!")
            enemy.hitpoints = enemy.hitpoints - damage

    def snipe(self):
        pass
    def heal(self):
        pass

    def run(self):

        self.is_running = True
        while self.is_running:

            #limit fps to fitty
            self.clock.tick(50)
            #turn loop

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
                            if item.text == 'Attack1':
                                self.funcs[item.text](self.infantry,self.enemy)
                            if item.text == 'Attack2':
                                self.funcs[item.text](self.medic,self.enemy)
                            if item.text == 'Attack3':
                                self.funcs[item.text](self.sniper,self.enemy)
                            if item.text == 'Melee':
                                self.funcs[item.text](self.infantry,self.enemy)
                            if item.text == 'Reload1':
                                self.funcs[item.text](self.infantry)
                            if item.text == 'Reload2':
                                self.funcs[item.text](self.medic)
                            if item.text == 'Reload3':
                                self.funcs[item.text](self.sniper)
                            if item.text == 'Heal':
                                self.funcs[item.text]()
                            if item.text == 'Snipe':
                                return

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

            #display player name
            self.display_name()
            #display the soldier name ammo health etc...
            self.display_labels()
            self.init_textbox()
            pygame.display.flip()
