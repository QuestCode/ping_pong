import sys
import pygame

from button import Button
from ball import  Ball
from game_stats import GameStats
from scoreboard import Scoreboard
from paddle import Paddle

TOPSCORE = 5

def new_game(ai_settings,screen):
    # Make the Play Button.
    play_button = Button(ai_settings,screen,"Play")

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    ball = Ball(ai_settings,screen)

    left_paddle = Paddle(ai_settings,screen, ai_settings.left_paddle_pos, ai_settings.left_paddle_score)
    right_paddle = Paddle(ai_settings,screen, ai_settings.right_paddle_pos, ai_settings.right_paddle_score)

    sb.left_score = left_paddle.score
    sb.right_score = right_paddle.score

    # start game loop
    while True:
        # check for keyboard or mouse events
        check_events(ai_settings,screen,stats,sb,play_button,ball,left_paddle,right_paddle)
        if stats.game_active:
            update_game(ai_settings,screen,sb,ball,left_paddle,right_paddle)
            check_for_winner(ai_settings,screen,left_paddle,right_paddle)
        update_screen(ai_settings,screen,stats,sb,ball,left_paddle,right_paddle,play_button)

def check_events(ai_settings,screen,stats,sb,play_button,ball,left_paddle,right_paddle):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,stats,sb,right_paddle)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,right_paddle)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,sb,ball,left_paddle,right_paddle,play_button,mouse_x,mouse_y)


def update_screen(ai_settings,screen,stats,sb,ball,left_paddle,right_paddle,play_button):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)

    update_score(sb,left_paddle,right_paddle)

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        initialize_game(ball,left_paddle,right_paddle)
        play_button.draw_button()
    else:
        allow_game_functions(ai_settings,screen,sb,ball,left_paddle,right_paddle)

    # Make the most recently drawn screen visible.
    pygame.display.flip()

def allow_game_functions(ai_settings,screen,sb,ball,left_paddle,right_paddle):
    ai_control(ai_settings,ball,left_paddle)
    update_game(ai_settings,screen,sb,ball,left_paddle,right_paddle)
    check_collision(ai_settings,screen,sb,ball,left_paddle,right_paddle)

def initialize_game(ball,left_paddle,right_paddle):
    ball.draw_ball()
    left_paddle.draw_paddle()
    right_paddle.draw_paddle()

def update_ball(ball):
    ball.update()
    ball.draw_ball()

def update_paddles(left_paddle,right_paddle):
    # Update paddles
    left_paddle.update()
    right_paddle.update()
    left_paddle.draw_paddle()
    right_paddle.draw_paddle()

def update_score(sb,left_paddle,right_paddle):
    sb.left_score = left_paddle.score
    sb.right_score = right_paddle.score
    sb.prep_score()
    # Draw the score information.
    sb.show_score()

def update_game(ai_settings,screen,sb,ball,left_paddle,right_paddle):
    update_ball(ball)
    update_paddles(left_paddle,right_paddle)


def check_keydown_events(event,ai_settings,screen,stats,sb,paddle):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
        # Move the paddle to the up
        paddle.vel = -ai_settings.user_paddle_vel
    elif event.key == pygame.K_DOWN:
        # Move the paddle to the down
        paddle.vel = ai_settings.user_paddle_vel
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p:
        start_game(ai_settings,stats,sb)

def check_keyup_events(event, paddle):
    if event.key == pygame.K_UP:
        paddle.vel = 0
    elif event.key == pygame.K_DOWN:
        paddle.vel = 0

def check_collision(ai_settings,screen,sb,ball, paddle1, paddle2):
    if ball.pos[0] <= paddle1.width*2 + ball.radius or ball.pos[0] >= ai_settings.screen_width - paddle1.width*2 - ball.radius:
        # Check if ball made contact with a paddle
        if (ball.pos[1] in range(paddle1.pos[1] - int(paddle1.height/2), paddle1.pos[1] + int(paddle1.height/2)) and ball.pos[0] < int(ai_settings.screen_width/2)):
            # Ball hit left paddle
            if ball.vel[0]<0:
                ball.vel[0] =- (ball.vel[0]-1)
                paddle1.play_sound()
            else:
                ball.vel[0] =- (ball.vel[0]+1)
        elif (ball.pos[1] in range(paddle2.pos[1] - int(paddle2.height/2), paddle2.pos[1] + int(paddle2.height/2)) and ball.pos[0] > int(ai_settings.screen_width/2)):
            if ball.vel[0]<0:
                ball.vel[0] =- (ball.vel[0]-1)
            # Ball hit left paddle
            else:
                ball.vel[0] =- (ball.vel[0]+1)
                paddle2.play_sound()

        else:
            # Check what side of the board the ball is on to determine who to give the point to
            if ball.pos[0]>int(ai_settings.screen_width/2):
                paddle1.score +=1
                ball.reset(ai_settings,screen,"Left")
            else:
                paddle2.score +=1
                ball.reset(ai_settings,screen,"Right")

def check_play_button(ai_settings,screen,stats,sb,ball,left_paddle,right_paddle,play_button,mouse_x,mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked:
        start_game(ai_settings,stats,sb)

def start_game(ai_settings,stats,sb):
    if not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True
        #
        # # Reset the scoreboard images.
        sb.prep_score()

def ai_control(ai_settings,ball,left_paddle):
    # If ball is moving away from paddle, center bat
    if ball.vel[0] > 0:
        if left_paddle.pos[1] < int(ai_settings.screen_height/2):
            left_paddle.vel = ai_settings.ai_paddle_vel
        elif left_paddle.pos[1] > int(ai_settings.screen_height/2):
            left_paddle.vel = -ai_settings.ai_paddle_vel
    # if ball moving towards paddle, track its movement.
    elif ball.vel[0] < 0:
        if left_paddle.pos[1] < ball.pos[1]:
            left_paddle.vel = ai_settings.ai_paddle_vel
        else :
            left_paddle.vel = -ai_settings.ai_paddle_vel

def display_win_msg(ai_settings,screen,player):
    screen.fill(ai_settings.bg_color)
    font = ai_settings.winner_font
    msg = font.render(player + " Wins", True, ai_settings.text_color)
    msgRect = msg.get_rect()
    msgRect.centerx = int(ai_settings.screen_width/2)
    msgRect.centery = int(ai_settings.screen_height/2)
    screen.blit(msg, msgRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                new_game(ai_settings,screen)
                return

def check_for_winner(ai_settings,screen,left_paddle,right_paddle):
    if left_paddle.score >= TOPSCORE:
        display_win_msg(ai_settings,screen, 'Player 1')
        return
    elif right_paddle.score >= TOPSCORE:
        display_win_msg(ai_settings,screen, 'Player 2')
        return
