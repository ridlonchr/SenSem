# As part of the Pitcher's Duel Project, I am conducting a comparative
# analysis of pygame GUI modules, and publishing the results on my blog.
# The comparison consists of implementing the same sample interface on
# each of the various GUIs.
#
# This code implements the interface using the Ocemp GUI library.  For
# details on this library, see:
# http://ocemp.sourceforge.net/guidoc.html
#
# The module author is: Marcus von Appen
#
# This source code is the work of David Keeney, dkeeney at travelbyroad dot net

#Import Modules
import pygame
from pygame.locals import *
import time
import math

# import gui stuff
from ocempgui.widgets import *
from ocempgui.widgets.components import TextListItem
from ocempgui.widgets.Constants import *

screenSize = (642, 429)

# define the necessary callback functions.
#  these are connected to signals within their respective
#  widgets, and invoked by the gui
#
def logAction(ed, text):
    """ add the text to the 'edit' window (callback function)"""
    ed.items.append(TextListItem(text))

def logButtonAction(ed, btn, text):
    """ add the button status to the 'edit' window (callback function)"""
    if btn.active:
        text += ' selected'
    else:
        text += ' deselected'
    #text += str(btn.active)
    ed.items.append(TextListItem(text))

def logTextAction(ed, txtWidget):
    """ add the text to the 'edit' window (callback function)"""
    text = txtWidget.text
    ed.items.append(TextListItem(text))

def logSlider(ed, slider):
    """ add the slider position to the 'edit' window (callback function)"""
    #text = str(slider.get_coords_from_value())
    text = 'Slider is at ' + str(int(slider.value)) + ' %'
    ed.items.append(TextListItem(text))

def progBar(pb, list):
    """ update progress bar for len of list (callback function)"""
    prog = len(list) / 20.0 * 100
    if prog > 100: prog = 100
    pb.set_value(prog)

# the body of the program is here
#
def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""

    #Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode(screenSize)
    pygame.display.set_caption('GUI Test - Ocemp')

    # create GUI object
    gui = Renderer()
    gui.screen = screen

    # create page label
    lbl = Label('Pygame GUI Test Page - Ocemp')
    lbl.position = 29, 13
    gui.add_widget(lbl)

    # create progress bar label
    lbl4 = Label('Progress Bar')
    lbl4.position = 356, 355
    gui.add_widget(lbl4)

    # progress bar
    pb = ProgressBar()
    pb.position = 354, 376
    gui.add_widget(pb)

    # create edit box
    ed = ScrolledList(250, 320)
    ed.scrolling = SCROLL_ALWAYS
    ed.items.append(TextListItem('tope of input'))
    ed.items.append(TextListItem('seconde of input'))
    ed.position = 367, 19
    gui.add_widget(ed)
    progBar(pb, ed.items) # update progress bar for above two items
    ed.connect_signal (SIG_LISTCHANGE, progBar, pb, ed.items)

    # create checkbuttons and add to gui
    cb1 = CheckButton ('Check Box #1')
    cb1.position = 52, 40
    cb1.connect_signal (SIG_CLICKED, logButtonAction, ed, cb1, 'Check Box #1 clicked')
    gui.add_widget(cb1)
    cb2 = CheckButton ('Check Box #2')
    cb2.position = 52, 70
    cb2.connect_signal (SIG_CLICKED, logButtonAction, ed, cb2, 'Check Box #2 clicked')
    gui.add_widget(cb2)
    cb3 = CheckButton ('Check Box #3')
    cb3.position = 52, 98
    cb3.connect_signal (SIG_CLICKED, logButtonAction, ed, cb3, 'Check Box #3 clicked')
    gui.add_widget(cb3)

    # create radio buttons, put in table, and add to gui
    rbTab = Table(3,1)
    rbTab.position = 210, 40
    rb1 = RadioButton('Radio Button #1', None)
    rb1.connect_signal (SIG_TOGGLED, logButtonAction, ed, rb1, 'Radio Button #1 ')
    rbTab.add_child(0, 0, rb1)
    rb2 = RadioButton('Radio Button #2', rb1)
    rb2.connect_signal (SIG_TOGGLED, logButtonAction, ed, rb2, 'Radio Button #2 ')
    rbTab.add_child(1, 0, rb2)
    rb3 = RadioButton('Radio Button #3', rb1)
    rb3.connect_signal (SIG_TOGGLED, logButtonAction, ed, rb3, 'Radio Button #3 ')
    rbTab.add_child(2, 0, rb3)
    gui.add_widget(rbTab)

    # create txt box label
    lbl2 = Label('Text Box')
    lbl2.position = 31, 130
    gui.add_widget(lbl2)

    # create text box
    en = Entry()
    en.position = 31, 155
    en.size = 250, 21
    en.connect_signal (SIG_INPUT, logTextAction, ed, en)
    gui.add_widget(en)

    # create slider label
    lbl3 = Label('Slider')
    lbl3.position = 31, 190
    gui.add_widget(lbl3)
    # create slider
    sl = HScale(0, 100, 1)
    sl.position = 31, 215
    sl.size = 200, 20
    sl.connect_signal (SIG_MOUSEUP, logSlider, ed, sl)
    gui.add_widget(sl)

    # add buttons, both regular and toggle
    btnTab = Table(2, 3)
    btnTab.position = 30, 250
    btnTab.spacing = 10
    btn1 = Button('Button 1')
    btn1.connect_signal (SIG_CLICKED, logAction, ed, 'Button 1 clicked')
    btnTab.add_child(0, 0, btn1)
    btn2 = Button('Button 2')
    btn2.connect_signal (SIG_CLICKED, logAction, ed, 'Button 2 clicked')
    btnTab.add_child(0, 1, btn2)
    btn3 = Button('Button 3')
    btn3.connect_signal (SIG_CLICKED, logAction, ed, 'Button 3 clicked')
    btnTab.add_child(0, 2, btn3)

    btnA = ToggleButton('Button A')
    btnA.connect_signal (SIG_TOGGLED, logButtonAction, ed, btnA, 'Button A ')
    btnTab.add_child(1, 0, btnA)
    btnB = ToggleButton('Button B')
    btnB.connect_signal (SIG_TOGGLED, logButtonAction, ed, btnB, 'Button B ')
    btnTab.add_child(1, 1, btnB)
    btnC = ToggleButton('Button C')
    btnC.connect_signal (SIG_TOGGLED, logButtonAction, ed, btnC, 'Button C ')
    btnTab.add_child(1, 2, btnC)
    gui.add_widget(btnTab)

    # create 'not implemented' label for image map
    lbl4 = Label('Image Map Not Implementable')
    lbl4.position = 31, 340
    gui.add_widget(lbl4)

    # make some insensitive
    btn2.sensitive = False
    cb3.sensitive = False

    #Main Loop
    while 1:

        #Handle Input Events
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                return

            # pass event to gui
            gui.distribute_events((event))

        # clear background, and draw clock-spinner
        screen.fill((250, 250, 250))
        radius = 30
        spinPos = 240, 362
        sp2 = spinPos[0]+1, spinPos[1]
        progressAngle = int(time.time() % 15 * 24 - 90) #60
        pygame.draw.circle(screen, (180, 180, 180), spinPos, radius, 0)
        for angle in range(-90, progressAngle):
            a = angle*math.pi/180
            tgt = radius*math.cos(a)+spinPos[0], \
                  radius*math.sin(a)+spinPos[1]
            pygame.draw.line(screen, (254,254,254), spinPos, tgt, 2)
        pygame.draw.circle(screen, (0,0,0), spinPos, radius, 2)
        pygame.draw.circle(screen, (0,0,0), spinPos, radius+1, 3)
        pygame.draw.circle(screen, (0,0,0), sp2, radius, 2)
        pygame.draw.circle(screen, (0,0,0), sp2, radius+1, 3)
        pygame.draw.line(screen, (0,0,0), spinPos, tgt, 2)
        tgt = spinPos[0], spinPos[1]-radius
        pygame.draw.line(screen, (0,0,0), spinPos, tgt, 2)

        # Draw GUI
        gui.update()
        gui.draw(gui.screen)

        pygame.display.flip()

main()
