import sys
import pygame

from settings import Settings

import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Pong')
    gf.new_game(ai_settings,screen)

run_game()
