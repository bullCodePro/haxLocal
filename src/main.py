import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, WHITE, RED, BLUE
from player import Player
from ball import Ball
from game import Game
from field import draw_field
from ui import draw_ui 

def resolve_player_collision(p1, p2):
    if p1.rect.colliderect(p2.rect):
        dx = p1.rect.centerx - p2.rect.centerx
        dy = p1.rect.centery - p2.rect.centery
        distance = pygame.Vector2(dx, dy)
        if distance.length() == 0:
            distance = pygame.Vector2(1, 0)
        overlap = p1.rect.width / 2
        push = distance.normalize() * overlap
        p1.rect.x += int(push.x / 2)
        p1.rect.y += int(push.y / 2)
        p2.rect.x -= int(push.x / 2)
        p2.rect.y -= int(push.y / 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Local HaxBall Clone")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 32, bold=True)

    game = Game()

    player1 = Player(100, 300, {
        'up': pygame.K_w,
        'down': pygame.K_s,
        'left': pygame.K_a,
        'right': pygame.K_d,
        'kick': pygame.K_SPACE
    }, RED)

    player2 = Player(800, 300, {
        'up': pygame.K_UP,
        'down': pygame.K_DOWN,
        'left': pygame.K_LEFT,
        'right': pygame.K_RIGHT,
        'kick': pygame.K_RETURN
    }, BLUE)

    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player1.handle_input(keys)
        player2.handle_input(keys)

        resolve_player_collision(player1, player2)

        ball.move()
        ball.collide_with_player(player1)
        ball.collide_with_player(player2)

        if keys[player1.controls['kick']]:
            ball.active_kick(player1)
        if keys[player2.controls['kick']]:
            ball.active_kick(player2)

        scored = game.check_goal(ball)
        if scored:
            ball.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            ball.velocity = pygame.Vector2(0, 0)
            player1.rect.topleft = (100, 300)
            player2.rect.topleft = (800, 300)

        draw_field(screen)
        draw_ui(screen, font, game.score[0], game.score[1], game.start_ticks) 
        player1.draw(screen)
        player2.draw(screen)
        ball.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
