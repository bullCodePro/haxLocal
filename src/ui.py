import pygame
from settings import SCREEN_WIDTH, WHITE, DARK_GRAY, RED, BLUE

def draw_ui(screen, font, red_score, blue_score, start_ticks):
    def render_score_ui():
        # Background bar
        bar_height = 50
        surface = pygame.Surface((SCREEN_WIDTH, bar_height), pygame.SRCALPHA)
        surface.fill(DARK_GRAY)

        # Timer
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        minutes = seconds // 60
        timer_str = f"{minutes:02}:{seconds % 60:02}"
        timer_font = pygame.font.SysFont("Arial", 28, bold=True)

        # Texts
        score_text = font.render(f"{red_score}  -  {blue_score}", True, WHITE)
        timer_text = timer_font.render(timer_str, True, WHITE)

        # Color boxes
        red_box = pygame.Surface((30, 30))
        red_box.fill(RED)
        blue_box = pygame.Surface((30, 30))
        blue_box.fill(BLUE)

        # Layout math
        spacing = 10
        total_width = red_box.get_width() + spacing + score_text.get_width() + spacing + blue_box.get_width() + spacing + timer_text.get_width()
        start_x = (SCREEN_WIDTH - total_width) // 2
        y = 10

        # Draw on internal surface
        surface.blit(red_box, (start_x, y))
        surface.blit(score_text, (start_x + red_box.get_width() + spacing, y))
        surface.blit(blue_box, (start_x + red_box.get_width() + spacing + score_text.get_width() + spacing, y))
        surface.blit(timer_text, (start_x + total_width - timer_text.get_width(), y))

        return surface

    # Draw top
    screen.blit(render_score_ui(), (0, 0))

    # Draw bottom, rotated
    rotated_ui = pygame.transform.rotate(render_score_ui(), 180)
    screen.blit(rotated_ui, (0, screen.get_height() - 50))
