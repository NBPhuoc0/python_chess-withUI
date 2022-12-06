import pygame, sys
from button import Button
from data.constants import *
import ChessMain
pygame.init()

screen = pygame.display.set_mode((WIDTH , HEIGHT))
screen.fill(pygame.Color('white'))
pygame.display.set_caption('Chess Game')

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Menu")

GAMEMODE = 1
global color1, color2
color1 = WHITE
color2 = GRAY  

BG = pygame.image.load("assets/Background.png")
def get_font(size): 
    return pygame.font.Font("assets/font.ttf", size)

def play(GSTATE):
    while True:
        ChessMain.GameStart(screen,1,2,GSTATE, color1, color2)
        pygame.display.update()

def Optionslevel(GSTATE = None):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        OPTIONS_Level1 = Button(image=None, pos=(330, 100), 
                            text_input="LEVEL 1", font=get_font(75), base_color="white", hovering_color="Green")
        OPTIONS_Level2 = Button(image=None, pos=(330, 250), 
                            text_input="LEVEL 2", font=get_font(75), base_color="white", hovering_color="Green")
        OPTIONS_Level3 = Button(image=None, pos=(330, 400), 
                            text_input="LEVEL 3", font=get_font(75), base_color="white", hovering_color="Green")
        OPTIONS_BACK = Button(image=None, pos=(330, 600), 
                    text_input="BACK", font=get_font(75), base_color="white", hovering_color="Green")
        for button in [OPTIONS_Level1, OPTIONS_Level2, OPTIONS_Level3, OPTIONS_BACK]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_Level1.checkForInput(OPTIONS_MOUSE_POS):
                    ChessMain.GameStart(screen,1, 2, None, color1, color2)
                if OPTIONS_Level2.checkForInput(OPTIONS_MOUSE_POS):
                    ChessMain.GameStart(screen,1, 3, None,color1, color2)
                if OPTIONS_Level3.checkForInput(OPTIONS_MOUSE_POS):
                    ChessMain.GameStart(screen,1, 4, None, color1, color2)
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(GSTATE)

        pygame.display.update()
def Color(GSTATE = None): 
    global color1, color2
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        BtnWhiteGRAY = Button(image=None, pos=(330, 100), 
                            text_input="WHITE - GRAY", font=get_font(50), base_color="white", hovering_color = "white")
        BtnWhiteCYAN = Button(image=None, pos=(330, 200), 
                            text_input="WHITE - CYAN", font=get_font(50), base_color="white", hovering_color = "white")
        BtnGRAYLiME = Button(image=None, pos=(330, 300), 
                        text_input="GRAY - LIME", font=get_font(50), base_color="white", hovering_color = "white")
        for button in [BtnWhiteGRAY, BtnWhiteCYAN, BtnGRAYLiME]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BtnWhiteGRAY.checkForInput(OPTIONS_MOUSE_POS):
                    color1 = WHITE
                    color2 = GRAY
                    main_menu(GSTATE)
                if BtnWhiteCYAN.checkForInput(OPTIONS_MOUSE_POS):
                    color1 = WHITE
                    color2 = CYAN
                    main_menu(GSTATE)
                if BtnGRAYLiME.checkForInput(OPTIONS_MOUSE_POS):
                    color1 = GRAY
                    color2 = LIME
                    main_menu(GSTATE)
                       
        pygame.display.update()
def options(GSTATE = None):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.blit(BG, (0, 0))

        OPTIONS_BACK = Button(image=None, pos=(330, 600), 
                            text_input="BACK", font=get_font(60), base_color="white", hovering_color="Green")
        OPTIONS_PvsAI = Button(image=None, pos=(330, 200), 
                            text_input="PlayerVsAI", font=get_font(60), base_color="white", hovering_color="Green")
        OPTIONS_AIvsAI = Button(image=None, pos=(330, 300), 
                            text_input="AI vs AI", font=get_font(60), base_color="white", hovering_color="Green")
        OPTIONS_COLOR = Button(image=None, pos=(330, 400), 
                            text_input="COLOR", font=get_font(60), base_color="white", hovering_color="Green")

        for button in [OPTIONS_BACK, OPTIONS_AIvsAI, OPTIONS_PvsAI, OPTIONS_COLOR]:
            button.changeColor(OPTIONS_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu(GSTATE)
                if OPTIONS_AIvsAI.checkForInput(OPTIONS_MOUSE_POS):
                    ChessMain.GameStart(screen, 2,3, None, color1, color2)
                if OPTIONS_PvsAI.checkForInput(OPTIONS_MOUSE_POS):
                    Optionslevel(GSTATE)
                if OPTIONS_COLOR.checkForInput(OPTIONS_MOUSE_POS):
                    Color(GSTATE)

        pygame.display.update()

def main_menu(GSTATE = None):
    while True:
        if GSTATE is not None:
            PLAY_BUTTON = Button(image=None, pos=(330, 250), 
                    text_input="CONTINUE", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")
        else:
            PLAY_BUTTON = Button(image=None, pos=(330, 250), 
                    text_input="NEWGAME", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(330, 100))


        OPTIONS_BUTTON = Button(image=None, pos=(330, 370), 
                            text_input="OPTIONS", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(image=None, pos=(330, 490), 
                            text_input="QUIT", font=get_font(50), base_color="#d7fcd4", hovering_color="Green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(GSTATE)
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options(GSTATE)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    main_menu()