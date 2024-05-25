import pygame
import sys
from level import Level
from overworld import Overworld
from settings import *
from ui import UI
from button import Button


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../assets/font.ttf", size)


def play():
    while True:
        pygame.mouse.get_pos()

        game.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock = pygame.time.Clock()
        clock.tick(120)


def main_menu():
    BG = pygame.image.load("../assets/Background.png")

    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("SUPER BOB BROS", True, "#FFFFFF")
        MENU_RECT = MENU_TEXT.get_rect(center=(800, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/BP.png"), pos=(800, 300),
                             text_input="JOGAR", font=get_font(55), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/BP.png"), pos=(800, 450),
                             text_input="SAIR", font=get_font(55), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


class Game:
    def __init__(self):

        # Atributos Iniciais do Jogo
        self.max_level = 0
        self.max_health = 100
        self.cur_health = 100
        self.coins = 0

        # Música
        self.level_bg_music = pygame.mixer.Sound('../audio/level_music.wav')
        self.overworld_bg_music = pygame.mixer.Sound('../audio/overworld_music.wav')

        # Criação da Tela de Fases'
        self.overworld = Overworld(0, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)

        # user interface
        self.ui = UI(screen)


    def create_level(self, current_level):
        self.level = Level(current_level, screen, self.create_overworld, self.change_coins, self.change_health,
                           self.max_level)
        self.status = 'level'
        self.overworld_bg_music.stop()
        self.level_bg_music.play(loops=-1)

    def create_overworld(self, current_level, new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.overworld = Overworld(current_level, self.max_level, screen, self.create_level)
        self.status = 'overworld'
        self.overworld_bg_music.play(loops=-1)
        self.level_bg_music.stop()

    def change_coins(self, amount):
        self.coins += amount

    def change_health(self, amount):
        self.cur_health += amount

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            self.coins = 0
            self.max_level = 0
            self.overworld = Overworld(0, self.max_level, screen, self.create_level)
            self.status = 'overworld'
            self.level_bg_music.stop()
            self.overworld_bg_music.play(loops=-1)

    def run(self):
        if self.status == 'overworld':
            self.overworld.run()
            self.coins = 0
            self.cur_health = 100
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_coins(self.coins)
            self.check_game_over()


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen2 = pygame.display.set_mode((1600, 900), pygame.FULLSCREEN)
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    main_menu()

    pygame.display.update()
    clock.tick(60)


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("../assets/font.ttf", size)


def play(self):
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("black")

        PLAY_TEXT = self.get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        screen.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460),
                           text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def options(self):
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("white")

        OPTIONS_TEXT = self.get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


def main_menu():
    BG = pygame.image.load("../assets/Background.png").convert()
    BG = pygame.transform.scale(BG(screen_width, screen_height))

    while True:
        screen.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("../assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("../assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game.run()
                    pygame.display.update()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock = pygame.time.Clock()
