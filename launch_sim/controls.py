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
            elif acceleration_active:
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
            elif angle_active:
                if event.key == pygame.K_RETURN:
                    try:
                        rocket_angle = input_angle
                        input_angle = ""
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    input_angle = input_angle[:-1]
                else:
                    input_angle += event.unicode
            elif thrust_active:
                if event.key == pygame.K_RETURN:
                    try:
                        rocket_thrust = input_thrust
                        input_thrust = ""
                    except ValueError:
                        pass
                elif event.key == pygame.K_BACKSPACE:
                    input_thrust = input_thrust[:-1]
                else:
                    input_thrust += event.unicode

    return True
