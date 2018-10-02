from custom_colors import Colors
import pygame

class Settings():
    """A class to store all settings for Ping Pong."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen Settings
        self.screen_width = 800
        self.screen_height = 600
        color = Colors()
        self.bg_color = color.black
        self.button_color = color.dark_gray
        self.text_color = color.white

        # Paddle settings
        self.paddle_width = 6
        self.paddle_height = int(self.screen_height/4)
        self.paddle_color = color.snow_white

        self.top_paddle_pos = [int(self.screen_width/2),int(self.paddle_width*2)]
        self.bottom_paddle_pos = [int(self.screen_width/2),int(self.screen_height-self.paddle_width*2)]
        self.left_paddle_pos = [int(self.paddle_width*2),int(self.screen_height/2)]
        self.right_paddle_pos = [int(self.screen_width-self.paddle_width*2),int(self.screen_height/2)]

        self.top_paddle_score = 0
        self.bottom_paddle_score = 0
        self.left_paddle_score = 0
        self.right_paddle_score = 0

        # Ball settings
        self.ball_color = color.snow_white
        self.ball_radius = 8

        self.user_paddle_vel = 3
        self.ai_paddle_vel = 2

        try:
            self.score_font = pygame.font.Font("fonts/impact.ttf", 50)
        except:
            self.score_font = pygame.font.Font(None, 50)

        try:
            self.winner_font = pygame.font.Font("fonts/impact.ttf", 70)
        except:
            self.winner_font = pygame.font.Font(None, 70)

    def play_winning_sound(self):
    	try:
    		pygame.mixer.music.load('sounds/winning_bell.aiff')
    		pygame.mixer.music.play()
    	except :
    		pass
