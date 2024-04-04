#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:50:10 2024

@author: asearer
"""

# rocket.py

import math

class Rocket:
    def __init__(self, x, y, velocity=5, acceleration=0.1, angle=0.0, thrust=1):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.acceleration = acceleration
        self.angle = angle
        self.thrust = thrust
        self.launched = False

    def update(self):
        if self.launched:
            self.velocity += self.acceleration
            self.y -= self.velocity * math.sin(math.radians(self.angle))
            self.x += self.velocity * math.cos(math.radians(self.angle))
