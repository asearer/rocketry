#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:54:45 2024

@author: asearer
"""

# controls.py

import pygame
import math

def handle_events(rocket, rocket_velocity, rocket_acceleration, rocket_angle, rocket_thrust):
    """
    Handle user input events.

    Parameters:
    - rocket (Rocket): The Rocket object in the simulation.
    - rocket_velocity (str): The string representation of rocket velocity.
    - rocket_acceleration (str): The string representation of rocket acceleration.
    - rocket_angle (str): The string representation of rocket angle.
    - rocket_thrust (str): The string representation of rocket thrust.

    Returns:
    - bool: True if the simulation should continue, False if the user wants to quit.
    """
    velocity_active = False
    acceleration_active = False
    angle_active = False
    thrust_active = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if mouse click is within input fields
            if velocity_rect.collidepoint(event.pos):
                velocity_active = True
                acceleration_active = False
                angle_active = False
                thrust_active = False
            elif acceleration_rect.collidepoint(event.pos):
                acceleration_active = True
                velocity_active = False
                angle_active = False
                thrust_active = False
            elif angle_rect.collidepoint(event.pos):
                angle_active = True
                velocity_active = False
                acceleration_active = False
                thrust_active = False
            elif thrust_rect.collidepoint(event.pos):
                thrust_active = True
                velocity_active = False
                acceleration_active = False
                angle_active = False

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
            # Similar logic for acceleration, angle, and thrust

    return True

