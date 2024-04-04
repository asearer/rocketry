#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:50:10 2024

@author: asearer
"""

# rocket.py

import math

class Rocket:
    """Represents a rocket object in the simulation."""

    def __init__(self, x, y, velocity=5, acceleration=0.1, angle=0.0, thrust=1):
        """
        Initializes a Rocket object.

        Parameters:
        - x (int): The x-coordinate of the rocket's initial position.
        - y (int): The y-coordinate of the rocket's initial position.
        - velocity (float): The initial velocity of the rocket.
        - acceleration (float): The acceleration rate of the rocket.
        - angle (float): The initial angle of the rocket's orientation.
        - thrust (int): The thrust of the rocket.
        """
        self.x = x
        self.y = y
        self.velocity = velocity
        self.acceleration = acceleration
        self.angle = angle
        self.thrust = thrust
        self.launched = False

    def update(self):
        """Update the rocket's position based on its velocity and angle."""
        if self.launched:
            self.velocity += self.acceleration
            self.y -= self.velocity * math.sin(math.radians(self.angle))
            self.x += self.velocity * math.cos(math.radians(self.angle))

