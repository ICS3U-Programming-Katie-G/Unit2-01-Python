#!/usr/bin/env python3

# Created By: Katie
# Date: September 22nd, 2022
# This program calculates the area and circumference of a circle with a set radius.


import math

radius = 4
area_circle = math.pi * radius**2
circumference_circle = math.pi * 2 * radius
print("The area of a circle with the radius of 4 is: {} mm^2".format(area_circle))
print(
    "The circumference of a circle with the radius of 4 is: {} mm".format(
        circumference_circle
    )
)
