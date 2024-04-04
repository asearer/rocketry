#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:50:53 2024

@author: asearer
"""

# main.py

import pygame
import sys
import math
from rocket import Rocket
from controls import handle_events

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FPS = 60

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Launch Simulation")
clock = pygame.time.Clock()

# Load rocket image
rocket_image = pygame.image.load("assets/rocket.png")
# Scale down the rocket image
rocket_image = pygame.transform.scale(rocket_image, (150, 150))  # Adjust the size as needed

# Font for text
font = pygame.font.Font(None, 36)

# Function to display text
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main loop
def main():
    rocket = Rocket(WIDTH // 2, HEIGHT)  # Default position

    rocket_velocity = ""
    rocket_acceleration = ""
    rocket_angle = ""
    rocket_thrust = ""

    input_velocity = ""
    input_acceleration = ""
    input_angle = ""
    input_thrust = ""

    running = True

    # Define input field rectangles
    velocity_rect = pygame.Rect(100, 140, 100, 30)
    acceleration_rect = pygame.Rect(100, 240, 100, 30)
    angle_rect = pygame.Rect(100, 340, 100, 30)
    thrust_rect = pygame.Rect(100, 440, 100, 30)

    # Define launch button rectangle
    launch_button_rect = pygame.Rect(10, 70, 120, 30)

    while running:
        running = handle_events(rocket, rocket_velocity, rocket_acceleration, rocket_angle, rocket_thrust)

        screen.fill(WHITE)

        # Draw Launch button
        pygame.draw.rect(screen, (0, 100, 0), launch_button_rect)
        draw_text("Launch", font, (255, 255, 255), launch_button_rect.x + 10, launch_button_rect.y + 5)

        # Draw text and input fields
        draw_text("Rocket Velocity:", font, (0, 0, 0), 10, 110)
        draw_text("Rocket Acceleration:", font, (0, 0, 0), 10, 210)
        draw_text("Rocket Angle:", font, (0, 0, 0), 10, 310)
        draw_text("Rocket Thrust:", font, (0, 0, 0), 10, 410)

        pygame.draw.rect(screen, (0, 0, 0), velocity_rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), acceleration_rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), angle_rect, 2)
        pygame.draw.rect(screen, (0, 0, 0), thrust_rect, 2)

        # Update rocket position and rotation
        rocket.update()

        # Display rocket
        rotated_rocket = pygame.transform.rotate(rocket_image, -rocket.angle)
        rocket_rect = rotated_rocket.get_rect(center=(rocket.x, rocket.y))
        screen.blit(rotated_rocket, rocket_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

