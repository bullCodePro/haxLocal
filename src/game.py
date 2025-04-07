import pygame
from settings import COURT_X, COURT_WIDTH, COURT_Y, COURT_HEIGHT, GOAL_HEIGHT

class Game:
    def __init__(self):
        self.goal_height = GOAL_HEIGHT
        self.goal_y = COURT_Y + (COURT_HEIGHT - self.goal_height) // 2

        # Allow a bit of margin to detect full goal entry
        self.left_goal_line = COURT_X - 5
        self.right_goal_line = COURT_X + COURT_WIDTH + 5

        self.score = [0, 0]  # [left team, right team]
        self.start_ticks = pygame.time.get_ticks()

    def check_goal(self, ball):
        # Right team scores (left goal)
        if (ball.rect.right < self.left_goal_line and
            self.goal_y < ball.rect.centery < self.goal_y + self.goal_height):
            self.score[1] += 1
            return 'right'

        # Left team scores (right goal)
        if (ball.rect.left > self.right_goal_line and
            self.goal_y < ball.rect.centery < self.goal_y + self.goal_height):
            self.score[0] += 1
            return 'left'

        return None
