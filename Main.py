import pygame
from pygame.locals import *
import random

# Initialize the game
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Brick Break Game")

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the paddle
paddle_width = 100
paddle_height = 20
paddle_x = window_width // 2 - paddle_width // 2
paddle_y = window_height - paddle_height - 10
paddle_speed = 5
paddle = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

# Set up the ball
ball_radius = 10
ball_x = window_width // 2
ball_y = window_height // 2
ball_dx = random.choice([-2, 2])
ball_dy = -2
ball = pygame.Rect(ball_x, ball_y, ball_radius, ball_radius)

# Set up the bricks
brick_width = 80
brick_height = 20
brick_rows = 5
brick_cols = window_width // brick_width
brick_color = [RED, GREEN, BLUE]
bricks = []
for row in range(brick_rows):
    for col in range(brick_cols):
        brick_x = col * brick_width
        brick_y = row * brick_height
        brick = pygame.Rect(brick_x, brick_y, brick_width, brick_height)
        bricks.append(brick)

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Move the paddle
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if keys[K_RIGHT] and paddle.right < window_width:
        paddle.right += paddle_speed

    # Move the ball
    ball.x += ball_dx
    ball.y += ball_dy

    # Check for collision with the paddle
    if ball.colliderect(paddle):
        ball_dy = -ball_dy

    # Check for collision with the bricks
    for brick in bricks:
        if ball.colliderect(brick):
            bricks.remove(brick)
            ball_dy = -ball_dy
            break

    # Check for collision with the walls
    if ball.left < 0 or ball.right > window_width:
        ball_dx = -ball_dx
    if ball.top < 0:
        ball_dy = -ball_dy

    # Draw the game objects
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, paddle)
    pygame.draw.circle(window, WHITE, (ball.x + ball_radius // 2, ball.y + ball_radius // 2), ball_radius)
    for brick in bricks:
        pygame.draw.rect(window, brick_color[random.randint(0, 2)], brick)

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()
