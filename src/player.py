import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, COURT_Y, COURT_HEIGHT

class Player:
    def __init__(self, x, y, controls, color):
        self.rect = pygame.Rect(x, y, 30, 30)
        self.controls = controls
        self.color = color
        self.speed = 5
        self.last_direction = pygame.Vector2(1, 0)

    def handle_input(self, keys):
        if keys[self.controls['up']]:
            self.rect.y -= self.speed
            self.last_direction = pygame.Vector2(0, -1)
        if keys[self.controls['down']]:
            self.rect.y += self.speed
            self.last_direction = pygame.Vector2(0, 1)
        if keys[self.controls['left']]:
            self.rect.x -= self.speed
            self.last_direction = pygame.Vector2(-1, 0)
        if keys[self.controls['right']]:
            self.rect.x += self.speed
            self.last_direction = pygame.Vector2(1, 0)

        # ✅ Clamp left/right to screen edges
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        # ✅ Clamp top/bottom with 70% soft limit based on COURT
        allowed_vertical_overlap = int(self.rect.height * 0.7)
        min_y = COURT_Y - allowed_vertical_overlap
        max_y = COURT_Y + COURT_HEIGHT - self.rect.height + allowed_vertical_overlap

        if self.rect.top < min_y:
            self.rect.top = min_y
        if self.rect.bottom > max_y + self.rect.height:
            self.rect.bottom = max_y + self.rect.height

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, self.rect)
