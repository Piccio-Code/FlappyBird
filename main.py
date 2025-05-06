import sys
import pygame

from settings import *
from Player import Player
from Obstacle import Obstacle
from Score import Score

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

pygame.display.set_caption("Piccio Bird")

is_active = True
lose_text = pygame.font.Font(None, 50)
play_again = pygame.font.Font(None, 30)

text = lose_text.render("YOU LOSE", True, "Black")
text1 = play_again.render("Press p to play again", True, "Black")

text_rect = text.get_rect(center = (screen.get_width() // 2, screen.get_height() // 2))
text1_rect = text1.get_rect(midtop = (text_rect.centerx, text_rect. bottom + 10))

background = pygame.image.load("sprites/background-day.png").convert_alpha()

ground = pygame.image.load("sprites/base.png")
ground_rect = ground.get_rect(bottomleft = (0, screen.get_height()))

player = Player(screen, ground_rect.top,"sprites/yellowbird-midflap.png")
pipe = Obstacle(screen, ground_rect.top, "sprites/pipe-green.png")
score = Score(screen)

obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 900)

obstacle_list: list[Obstacle] = []

while True:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == obstacle_timer and is_active:
            obstacle = Obstacle(screen, ground_rect.top, "sprites/pipe-green.png")
            obstacle.create()
            obstacle_list.append(obstacle)
            score.add()

    if is_active:
        screen.blit(ground, ground_rect)

        for obstacle in obstacle_list:
            obstacle.render()

        player.render()
        score.render()

        for obstacle in obstacle_list:
            if obstacle.collide_with(player.rect):
                obstacle_list = []
                is_active = False
                continue

        for i, obstacle in enumerate(obstacle_list):
            if not obstacle.in_scene():
                obstacle_list.pop(i)
    else:
        keys = pygame.key.get_pressed()

        score.score = 0

        screen.blit(text, text_rect)
        screen.blit(text1, text1_rect)

        if keys[pygame.K_p]:
            is_active = True

    pygame.display.update()
    clock.tick(65)