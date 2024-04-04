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
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60
GRAVITY = 0.1

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Launch Simulation")
clock = pygame.time.Clock()

# Font for text
font = pygame.font.Font(None, 36)

# Rocket class
class Rocket:
    def __init__(self, x, y, velocity, acceleration, angle, length, radius):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.acceleration = acceleration
        self.angle = angle
        self.length = length
        self.radius = radius

    def update(self):
        self.velocity += self.acceleration
        self.y -= self.velocity * math.sin(math.radians(self.angle))
        self.x += self.velocity * math.cos(math.radians(self.angle))
        # Draw rocket wireframe
        points = []
        for angle in range(0, 360, 10):
            x = self.x + self.radius * math.cos(math.radians(angle))
            y = self.y + self.radius * math.sin(math.radians(angle))
            points.append((x, y))
        pygame.draw.lines(screen, BLACK, True, points, 2)
        # Draw rocket nose
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x + self.length * math.cos(math.radians(self.angle)), self.y - self.length * math.sin(math.radians(self.angle))), 2)

# Function to display text
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Main loop
def main():
    rocket_velocity = ""
    rocket_acceleration = ""

    input_velocity = ""
    input_acceleration = ""
    velocity_active = False
    acceleration_active = False

    # Larger rocket
    rocket = Rocket(WIDTH // 2, HEIGHT, 0, 0, 90, 70, 15)  # Initial angle set to 90 degrees, length = 70, radius = 15
    running = True

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
            elif event.type == pygame.MOUSEMOTION:
                # Check if mouse is being dragged to adjust angle
                if pygame.mouse.get_pressed()[0]:  # Left mouse button
                    rocket.angle = math.degrees(math.atan2(event.pos[1] - rocket.y, event.pos[0] - rocket.x))
                    # Update rocket position
                    rocket.x = event.pos[0] - rocket.length * math.cos(math.radians(rocket.angle))
                    rocket.y = event.pos[1] + rocket.length * math.sin(math.radians(rocket.angle))
            elif event.type == pygame.KEYDOWN:
                if velocity_active:
                    if event.key == pygame.K_RETURN:
                        try:
                            rocket.velocity = float(input_velocity)
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
                            rocket.acceleration = float(input_acceleration)
                            input_acceleration = ""
                        except ValueError:
                            pass
                    elif event.key == pygame.K_BACKSPACE:
                        input_acceleration = input_acceleration[:-1]
                    else:
                        input_acceleration += event.unicode

        screen.fill(WHITE)

        # Display input fields
        velocity_rect = pygame.draw.rect(screen, BLACK, (100, 100, 200, 50), 2)
        acceleration_rect = pygame.draw.rect(screen, BLACK, (100, 200, 200, 50), 2)

        draw_text("Rocket Velocity:", font, BLACK, 10, 110)
        if velocity_active:
            draw_text(input_velocity, font, BLACK, 105, 110)
        else:
            draw_text(rocket_velocity, font, BLACK, 105, 110)

        draw_text("Rocket Acceleration:", font, BLACK, 10, 210)
        if acceleration_active:
            draw_text(input_acceleration, font, BLACK, 105, 210)
        else:
            draw_text(rocket_acceleration, font, BLACK, 105, 210)

        # Update rocket
        rocket.update()

        # Check if rocket reaches the top or bottom of the screen
        if rocket.y <= 0 or rocket.y >= HEIGHT:
            rocket.velocity *= -0.9  # Reverse velocity with some loss
            rocket.acceleration *= -0.9  # Reverse acceleration

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
