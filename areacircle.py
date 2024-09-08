# Question: Write a program in Python to find the area of a circle.

import math

def circle_area(radius):
    # Area of a circle formula: π * r^2
    area = math.pi * (radius ** 2)
    return area

# Example usage:
radius = 5
area = circle_area(radius)
print(f"Area of the circle with radius {radius}cm: {area} square cm")
