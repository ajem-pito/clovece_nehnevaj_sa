import pygame as pg
from pygame import mixer

class Zvuk:
    ...


import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Title")

# Font settings
font = pygame.font.Font(None, 36)
text = font.render("Moving Title", True, (255, 255, 255))

# Text position and movement speed
text_x = 0
text_y = screen_height // 2
text_speed = 2

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update text position
    text_x += text_speed

    # If the text goes off the screen, reset its position to the left
    if text_x > screen_width:
        text_x = -text.get_width()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Blit the text onto the screen
    screen.blit(text, (text_x, text_y))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
