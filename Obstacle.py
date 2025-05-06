import pygame
import random


class Obstacle:
    def __init__(self, screen: pygame.Surface, ground: int, path: str):
        self.screen = screen
        self.ground = ground

        self.pipe_image = pygame.image.load(path).convert_alpha()

        self.top = None
        self.bottom = None

        self.top_rect = None
        self.bottom_rect = None

        self.obstacle = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        self.rect = self.obstacle.get_rect()

    def create(self):
        x = self.screen.get_width() + random.randint(100, 200)

        space = random.randint(100, 150)
        height = random.randint(100, self.ground - space - 100)

        width = self.pipe_image.get_width()

        self.bottom = pygame.Surface((width, height), pygame.SRCALPHA)
        self.bottom.blit(self.pipe_image, (0, 0))

        self.bottom_rect = self.bottom.get_rect(midbottom=(x, self.ground))

        self.top = pygame.Surface((width, (self.ground - height - space)), pygame.SRCALPHA)
        self.top.blit(self.pipe_image, (0, 0))
        self.top = pygame.transform.rotate(self.top, 180)

        self.top_rect = self.top.get_rect(midtop=(x, 0))

    def move(self):
        self.top_rect.x -= 3
        self.bottom_rect.x -= 3


    def render(self):
        self.move()

        self.screen.blit(self.top, self.top_rect)
        self.screen.blit(self.bottom, self.bottom_rect)

    def in_scene(self):
        if self.top_rect.x <= -100:
            return False

        return True

    def collide_with(self, player: pygame.Rect):
        return self.top_rect.colliderect(player) or self.bottom_rect.colliderect(player)
