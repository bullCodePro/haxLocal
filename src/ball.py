import pygame
from settings import YELLOW, COURT_X, COURT_Y, COURT_WIDTH, COURT_HEIGHT, GOAL_HEIGHT

class Ball:
    def __init__(self, x, y):
        self.radius = 8
        self.rect = pygame.Rect(x, y, self.radius * 2, self.radius * 2)
        self.color = YELLOW
        self.velocity = pygame.Vector2(0, 0)

    def move(self):
        self.rect.x += int(self.velocity.x)
        self.rect.y += int(self.velocity.y)

        self.velocity *= 0.983  # Friction

        # Bounds
        left_wall = COURT_X
        right_wall = COURT_X + COURT_WIDTH
        top_wall = COURT_Y
        bottom_wall = COURT_Y + COURT_HEIGHT

        goal_y = COURT_Y + (COURT_HEIGHT - GOAL_HEIGHT) // 2

        # Left wall bounce — block only outside goal
        if self.rect.left <= left_wall:
            if not (goal_y < self.rect.centery < goal_y + GOAL_HEIGHT):
                self.rect.left = left_wall
                self.velocity.x *= -1

        # Right wall bounce — block only outside goal
        if self.rect.right >= right_wall:
            if not (goal_y < self.rect.centery < goal_y + GOAL_HEIGHT):
                self.rect.right = right_wall
                self.velocity.x *= -1

        # Top and bottom
        if self.rect.top <= top_wall:
            self.rect.top = top_wall
            self.velocity.y *= -1
        if self.rect.bottom >= bottom_wall:
            self.rect.bottom = bottom_wall
            self.velocity.y *= -1

    def collide_with_player(self, player):
        if self.rect.colliderect(player.rect):
            push_direction = pygame.Vector2(
                self.rect.centerx - player.rect.centerx,
                self.rect.centery - player.rect.centery
            )
            if push_direction.length() != 0:
                self.velocity += push_direction.normalize() * 2

    def active_kick(self, player):
        if self.rect.colliderect(player.rect):
            direction = player.last_direction.normalize()
            self.velocity += direction * 5

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius)
