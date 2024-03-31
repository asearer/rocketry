#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:43:26 2024

@author: asearer
"""

import math
import tkinter as tk
from tkinter import messagebox

def convert_to_meters(value, unit):
    if unit == "m":
        return value
    elif unit == "cm":
        return value / 100
    elif unit == "mm":
        return value / 1000

def calculate_volume(radius, length):
    return math.pi * radius**2 * length

def calculate_surface_area(radius, length):
    return 2 * math.pi * radius * (radius + length)

def calculate_mass(volume, density):
    return volume * density

def calculate_center_of_gravity(length):
    return length / 2

def calculate_rocket_specifications(radius, length, radius_unit, length_unit):
    density_of_rocket_body = 1300  # kg/m^3 (typical density of rocket body)

    radius_m = convert_to_meters(radius, radius_unit)
    length_m = convert_to_meters(length, length_unit)

    volume = calculate_volume(radius_m, length_m)
    surface_area = calculate_surface_area(radius_m, length_m)
    mass = calculate_mass(volume, density_of_rocket_body)
    center_of_gravity = calculate_center_of_gravity(length_m)

    return volume, surface_area, mass, center_of_gravity

def calculate_button_clicked():
    try:
        radius = float(radius_entry.get())
        radius_unit = radius_unit_var.get()
        length = float(length_entry.get())
        length_unit = length_unit_var.get()

        volume, surface_area, mass, center_of_gravity = calculate_rocket_specifications(radius, length, radius_unit, length_unit)

        volume_label.config(text="Volume: {:.3f} cubic meters".format(volume))
        surface_area_label.config(text="Surface Area: {:.3f} square meters".format(surface_area))
        mass_label.config(text="Mass: {:.3f} kilograms".format(mass))
        center_of_gravity_label.config(text="Center of Gravity: {:.3f} meters from the base".format(center_of_gravity))
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for radius and length.")

# Create main window
root = tk.Tk()
root.title("Solid-Fueled Hobby Rocket Calculator")

# Create labels and entry widgets
radius_label = tk.Label(root, text="Enter the radius of the rocket tube:")
radius_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
radius_entry = tk.Entry(root)
radius_entry.grid(row=0, column=1, padx=5, pady=5)

radius_unit_var = tk.StringVar(root)
radius_unit_var.set("m")
radius_unit_options = ["m", "cm", "mm"]
radius_unit_menu = tk.OptionMenu(root, radius_unit_var, *radius_unit_options)
radius_unit_menu.grid(row=0, column=2, padx=5, pady=5)

length_label = tk.Label(root, text="Enter the length of the rocket tube:")
length_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=5, pady=5)

length_unit_var = tk.StringVar(root)
length_unit_var.set("m")
length_unit_options = ["m", "cm", "mm"]
length_unit_menu = tk.OptionMenu(root, length_unit_var, *length_unit_options)
length_unit_menu.grid(row=1, column=2, padx=5, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_button_clicked)
calculate_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

volume_label = tk.Label(root, text="")
volume_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

surface_area_label = tk.Label(root, text="")
surface_area_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

mass_label = tk.Label(root, text="")
mass_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

center_of_gravity_label = tk.Label(root, text="")
center_of_gravity_label.grid(row=6, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
