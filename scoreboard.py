import pygame.font

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self,ai_settings, screen, stats):
        """Initialize scorekeeping attribute."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = ai_settings.text_color
        self.font = pygame.font.SysFont(None,48)

        self.left_score = ai_settings.left_paddle_score
        self.right_score = ai_settings.right_paddle_score
        self.top_score = ai_settings.top_paddle_score
        self.bottom_score = ai_settings.bottom_paddle_score

        # Prepare the initial score images.
        self.prep_score()

    def prep_score(self):
        """Turn the score into a rendered image."""
        font = self.ai_settings.score_font
        self.player1_msg = font.render('Player 1', True, self.text_color)
        self.player2_msg = font.render('Player 2', True, self.text_color)
        self.player3_msg = font.render('Player 3', True, self.text_color)
        self.player4_msg = font.render('Player 4', True, self.text_color)
        self.left_score_msg = font.render(str(self.left_score), True,self.text_color)
        self.right_score_msg = font.render(str(self.right_score), True,self.text_color)
        self.bottom_score_msg = font.render(str(self.bottom_score), True,self.text_color)
        self.top_score_msg = font.render(str(self.top_score), True,self.text_color)

        score_rect_width = self.ai_settings.screen_width/4
        score_rect_height = self.ai_settings.screen_height/4

        # Player Title Score
        self.player1_msg_rect = self.player1_msg.get_rect()
        self.player2_msg_rect = self.player2_msg.get_rect()
        self.player3_msg_rect = self.player3_msg.get_rect()
        self.player4_msg_rect = self.player4_msg.get_rect()

        self.player1_msg_rect.left = int(score_rect_width/1.5)
        self.player2_msg_rect.left = int(score_rect_width*2.7)
        self.player3_msg_rect.left = int(score_rect_width/1.5)
        self.player4_msg_rect.left = int(score_rect_width*2.7)

        self.player1_msg_rect.top = int(score_rect_height/3)
        self.player2_msg_rect.top = int(score_rect_height/3)
        self.player3_msg_rect.bottom = int(score_rect_height*2.9)
        self.player4_msg_rect.bottom = int(score_rect_height*2.9)

        # Display the score at the top right of the screen.
        self.left_score_msg_rect = self.left_score_msg.get_rect()
        self.right_score_msg_rect = self.right_score_msg.get_rect()
        self.top_score_msg_rect = self.top_score_msg.get_rect()
        self.bottom_score_msg_rect = self.bottom_score_msg.get_rect()

        self.left_score_msg_rect.left = int(score_rect_width)
        self.right_score_msg_rect.left = int(score_rect_width * 3)
        self.left_score_msg_rect.top = int(score_rect_height)
        self.right_score_msg_rect.top = int(score_rect_height)

        self.top_score_msg_rect.left = int(score_rect_width)
        self.bottom_score_msg_rect.left = int(score_rect_width * 3)
        self.top_score_msg_rect.bottom = int(score_rect_height*3.5)
        self.bottom_score_msg_rect.bottom = int(score_rect_height*3.5)

    def show_score(self):
        """Draw score to the screen."""
        self.screen.blit(self.left_score_msg,self.left_score_msg_rect)
        self.screen.blit(self.right_score_msg,self.right_score_msg_rect)
        self.screen.blit(self.player1_msg,self.player1_msg_rect)
        self.screen.blit(self.player2_msg,self.player2_msg_rect)

        self.screen.blit(self.top_score_msg,self.top_score_msg_rect)
        self.screen.blit(self.bottom_score_msg,self.bottom_score_msg_rect)
        self.screen.blit(self.player3_msg,self.player3_msg_rect)
        self.screen.blit(self.player4_msg,self.player4_msg_rect)
