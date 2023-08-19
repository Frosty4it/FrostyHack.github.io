import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slope Game")

# Ball properties
ball_radius = 20
ball_color = RED
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed = 5
ball_velocity = [0, 0]

# Gravity
gravity = 0.2

# Obstacle properties
obstacle_width = 100
obstacle_height = 20
obstacle_color = BLACK
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the ball based on user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ball_velocity[0] -= ball_speed
    if keys[pygame.K_RIGHT]:
        ball_velocity[0] += ball_speed

    # Apply gravity
    ball_velocity[1] += gravity

    # Update ball position
    ball_x += ball_velocity[0]
    ball_y += ball_velocity[1]

    # Check for collision with the ground
    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity[1] = 0

    # Update obstacle position
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, WIDTH - obstacle_width)

    # Check for collision with the obstacle
    if (ball_x + ball_radius > obstacle_x and ball_x - ball_radius < obstacle_x + obstacle_width) and \
            (ball_y + ball_radius > obstacle_y and ball_y - ball_radius < obstacle_y + obstacle_height):
        print("Game Over!")
        running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the ball and obstacle
    pygame.draw.circle(screen, ball_color, (int(ball_x), int(ball_y)), ball_radius)
    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()
