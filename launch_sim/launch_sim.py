#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:05:43 2024

@author: asearer
"""

import pygame
import sys
import math

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
rocket_image = pygame.image.load("rocket.png")
# Scale down the rocket image
rocket_image = pygame.transform.scale(rocket_image, (150, 150))  # Adjust the size as needed 150 is good for demo

# Font for text
font = pygame.font.Font(None, 36)

# Rocket class
class Rocket:
    def __init__(self, x, y, velocity, acceleration, angle):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.acceleration = acceleration
        self.angle = angle

    def update(self):
        self.velocity += self.acceleration
        self.y -= self.velocity * math.sin(math.radians(self.angle))
        self.x += self.velocity * math.cos(math.radians(self.angle))

# Function to display text
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to draw button
def draw_button(text, font, color, rect):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

# Main loop
def main():
    rocket_velocity = ""
    rocket_acceleration = ""

    input_velocity = ""
    input_acceleration = ""
    velocity_active = False
    acceleration_active = False

    rocket = Rocket(WIDTH // 2, HEIGHT, 0, 0, 90)  # Initial angle set to 90 degrees
    running = True

    # Define launch button rectangle
    launch_button_rect = pygame.Rect(10, 70, 120, 30)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if mouse click is within input fields
                if velocity_rect.collidepoint(event.pos):
                    velocity_active = True
                    acceleration_active = False
                elif acceleration_rect.collidepoint(event.pos):
                    acceleration_active = True
                    velocity_active = False
                else:
                    velocity_active = False
                    acceleration_active = False
                # Check if mouse click is within launch button
                if launch_button_rect.collidepoint(event.pos):
                    # Launch the rocket with current parameters
                    try:
                        rocket.velocity = float(rocket_velocity)
                        rocket.acceleration = float(rocket_acceleration)
                    except ValueError:
                        pass
            elif event.type == pygame.MOUSEMOTION:
                # Check if mouse is being dragged to adjust angle
                if pygame.mouse.get_pressed()[0]:  # Left mouse button
                    rocket.angle = math.degrees(math.atan2(event.pos[1] - rocket.y, event.pos[0] - rocket.x))
            elif event.type == pygame.KEYDOWN:
                if velocity_active:
                    if event.key == pygame.K_RETURN:
                        try:
                            rocket_velocity = input_velocity
                            input_velocity = ""
                        except ValueError:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        input_velocity = input_velocity[:-1]
                    else:
                        input_velocity += event.unicode
                if acceleration_active:
                    if event.key == pygame.K_RETURN:
                        try:
                            rocket_acceleration = input_acceleration
                            input_acceleration = ""
                        except ValueError:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        input_acceleration = input_acceleration[:-1]
                    else:
                        input_acceleration += event.unicode

        screen.fill(WHITE)

        # Display Launch button
        draw_button("Launch", font, (0, 100, 0), launch_button_rect)

        # Display text and input fields
        draw_text("Rocket Velocity:", font, (0, 0, 0), 10, 110)
        velocity_rect = pygame.draw.rect(screen, (0, 0, 0), (100, 140, 100, 30), 2)  # Adjusted x-coordinate
        if velocity_active:
            draw_text(input_velocity, font, (0, 0, 0), 105, 150)  # Adjusted x-coordinate
        else:
            draw_text(rocket_velocity, font, (0, 0, 0), 105, 150)  # Adjusted x-coordinate

        draw_text("Rocket Acceleration:", font, (0, 0, 0), 10, 210)
        acceleration_rect = pygame.draw.rect(screen, (0, 0, 0), (100, 240, 100, 30), 2)  # Adjusted x-coordinate
        if acceleration_active:
            draw_text(input_acceleration, font, (0, 0, 0), 105, 250)  # Adjusted x-coordinate
        else:
            draw_text(rocket_acceleration, font, (0, 0, 0), 105, 250)  # Adjusted x-coordinate

        # Update rocket
        rotated_rocket = pygame.transform.rotate(rocket_image, rocket.angle)
        rocket_rect = rotated_rocket.get_rect(center=(rocket.x, rocket.y))
        screen.blit(rotated_rocket, rocket_rect)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
