import pygame
import random

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH = 800
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cookie Clicker")

# Font
font = pygame.font.Font(None, 36)

# Cookie properties
cookie_size = 100
cookie_x = WIDTH // 2 - cookie_size // 2
cookie_y = HEIGHT // 2 - cookie_size // 2

# Upgrade properties
upgrade_cost = 10
click_multiplier = 1
upgrade_level = 1

# Game loop
cookies = 0
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the cookie was clicked
            if cookie_x < event.pos[0] < cookie_x + cookie_size and \
                    cookie_y < event.pos[1] < cookie_y + cookie_size:
                cookies += click_multiplier

    # Clear the screen
    screen.fill(WHITE)

    # Draw the cookie
    pygame.draw.circle(screen, GRAY, (cookie_x + cookie_size // 2, cookie_y + cookie_size // 2), cookie_size // 2)
    pygame.draw.circle(screen, BLACK, (cookie_x + cookie_size // 2, cookie_y + cookie_size // 2), cookie_size // 2, 5)

    # Draw the UI
    cookie_count_text = font.render("Cookies: " + str(cookies), True, BLACK)
    screen.blit(cookie_count_text, (20, 20))

    upgrade_text = font.render(f"Upgrade (Cost: {upgrade_cost})", True, BLACK)
    screen.blit(upgrade_text, (20, 60))

    # Check if player can afford upgrade
    if cookies >= upgrade_cost:
        pygame.draw.rect(screen, BLACK, (20, 100, 200, 40))
        upgrade_button = font.render("Upgrade", True, WHITE)
        screen.blit(upgrade_button, (25, 105))

    # Update the display
    pygame.display.flip()

    # Check for upgrade click
    if pygame.mouse.get_pressed()[0]:
        if cookies >= upgrade_cost and 20 <= pygame.mouse.get_pos()[0] <= 220 and \
                100 <= pygame.mouse.get_pos()[1] <= 140:
            cookies -= upgrade_cost
            click_multiplier += 1
            upgrade_level += 1
            upgrade_cost = 10 * upgrade_level

    # Cap the frame rate
    clock.tick(60)

# Clean up
pygame.quit()