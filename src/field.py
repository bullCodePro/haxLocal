import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, DARK_GRAY, GOAL_HEIGHT

# Define margins around the field
MARGIN_X = 50
MARGIN_Y = 50
COURT_WIDTH = SCREEN_WIDTH - 2 * MARGIN_X
COURT_HEIGHT = SCREEN_HEIGHT - 2 * MARGIN_Y
COURT_X = MARGIN_X
COURT_Y = MARGIN_Y

def draw_field(screen):
    screen.fill(DARK_GRAY)

    wall_thickness = 6
    goal_width = 10
    goal_y = COURT_Y + (COURT_HEIGHT - GOAL_HEIGHT) // 2
    net_depth = 30  # how far the net goes outside the field

    # Top and bottom walls
    pygame.draw.rect(screen, WHITE, (COURT_X, COURT_Y, COURT_WIDTH, wall_thickness))  # Top
    pygame.draw.rect(screen, WHITE, (COURT_X, COURT_Y + COURT_HEIGHT - wall_thickness, COURT_WIDTH, wall_thickness))  # Bottom

    # Left wall with gap
    pygame.draw.rect(screen, WHITE, (COURT_X, COURT_Y, wall_thickness, goal_y - COURT_Y))
    pygame.draw.rect(screen, WHITE, (COURT_X, goal_y + GOAL_HEIGHT, wall_thickness, COURT_Y + COURT_HEIGHT - (goal_y + GOAL_HEIGHT)))

    # Right wall with gap
    right_x = COURT_X + COURT_WIDTH - wall_thickness
    pygame.draw.rect(screen, WHITE, (right_x, COURT_Y, wall_thickness, goal_y - COURT_Y))
    pygame.draw.rect(screen, WHITE, (right_x, goal_y + GOAL_HEIGHT, wall_thickness, COURT_Y + COURT_HEIGHT - (goal_y + GOAL_HEIGHT)))

    # Center line
    pygame.draw.line(screen, WHITE,
        (COURT_X + COURT_WIDTH // 2, COURT_Y),
        (COURT_X + COURT_WIDTH // 2, COURT_Y + COURT_HEIGHT), 2)

    # Center circle and dot
    center = (COURT_X + COURT_WIDTH // 2, COURT_Y + COURT_HEIGHT // 2)
    pygame.draw.circle(screen, WHITE, center, 60, 2)
    pygame.draw.circle(screen, WHITE, center, 5)

    # Left goal post
    pygame.draw.rect(screen, WHITE, (COURT_X, goal_y, goal_width, GOAL_HEIGHT))

    # Right goal post
    pygame.draw.rect(screen, WHITE, (COURT_X + COURT_WIDTH - goal_width, goal_y, goal_width, GOAL_HEIGHT))

    # Left U-shaped solid goal net
    pygame.draw.line(screen, WHITE, (COURT_X, goal_y), (COURT_X - net_depth, goal_y), 2)  # top bar
    pygame.draw.line(screen, WHITE, (COURT_X - net_depth, goal_y), (COURT_X - net_depth, goal_y + GOAL_HEIGHT), 2)  # back post
    pygame.draw.line(screen, WHITE, (COURT_X - net_depth, goal_y + GOAL_HEIGHT), (COURT_X, goal_y + GOAL_HEIGHT), 2)  # bottom bar

    # Right U-shaped solid goal net
    rx = COURT_X + COURT_WIDTH
    pygame.draw.line(screen, WHITE, (rx, goal_y), (rx + net_depth, goal_y), 2)  # top bar
    pygame.draw.line(screen, WHITE, (rx + net_depth, goal_y), (rx + net_depth, goal_y + GOAL_HEIGHT), 2)  # back post
    pygame.draw.line(screen, WHITE, (rx + net_depth, goal_y + GOAL_HEIGHT), (rx, goal_y + GOAL_HEIGHT), 2)  # bottom bar
