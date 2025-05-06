from selectors import SelectSelector

import pygame
import math

class Score:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen

        self.score = 0

        self.nums = []

        for i in range(10):
            self.nums.append(pygame.image.load(f"sprites/{i}.png"))

    def add(self):
        self.score += 1

    def render(self):
        score_img = pygame.Surface((25 * int(math.log(self.score, 10) + 1 if self.score else 1), 36), pygame.SRCALPHA)
        score_rect = score_img.get_rect(center = (self.screen.get_width() // 2, 100))
        digits = []
        temp = self.score

        if not temp:
            digits.append(self.nums[0])
        else:
            while temp > 0:
                digits.append(self.nums[int(temp%10)])
                temp = temp // 10

            digits.reverse()

        for i, digit in enumerate(digits):
            score_img.blit(digit, (i * 25, 0))

        self.screen.blit(score_img, score_rect)