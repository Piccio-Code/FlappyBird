import pygame

class Player:
    def __init__(self, screen: pygame.Surface, ground: int, path: str):
        self.screen = screen

        img = (pygame.image.load(path)).convert_alpha()
        self.player = pygame.Surface((img.get_width(), img.get_height()), pygame.SRCALPHA)
        self.player.blit(img, (0, 0))
        self.rect = self.player.get_rect(center = (screen.get_width()//2, screen.get_height()//2))

        self.downforce = 0
        self.ground = ground

    def gravity(self):
        self.downforce += .3
        self.rect.centery += self.downforce

        self.rect.bottom = min(self.rect.bottom, self.ground)
        self.rect.top = max(self.rect.top, 0)

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.downforce = -4

    def render(self):
        self.screen.blit(self.player, self.rect)
        self.gravity()
        self.movement()
