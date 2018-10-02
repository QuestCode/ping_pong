import pygame, random


class Ball():
    """ Class to keep track of a ball's location and vector."""
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.screen_height = ai_settings.screen_height
        self.radius = ai_settings.ball_radius
        self.color  = ai_settings.ball_color

        self.reset(ai_settings,screen,"Left")

    def reset(self,ai_settings,screen,direction):
        # Place ball at the center of the screen
        self.pos = [int(ai_settings.screen_width/2),int(ai_settings.screen_height/2)]
        if direction == "Right":
            self.vel = [random.randint(2,4),-random.randint(1,3)]
        elif direction == "Left":
            self.vel = [-random.randint(2,4),-random.randint(1,3)]
        elif direction == "Top":
            self.vel = [random.randint(2,4),random.randint(1,3)]
        elif direction == "Bottom":
            self.vel = [random.randint(2,4),-random.randint(1,3)]

    def draw_ball(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)

    def update(self):
        """Move the ball postion on the screen."""
        # Check if ball made contact with the wall
        if self.pos[1] <= self.radius or self.pos[1] >= self.screen_height-self.radius:			# If the ball hits walls
            self.vel[1] = -self.vel[1]
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]
