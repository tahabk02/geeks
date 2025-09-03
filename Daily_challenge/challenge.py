import math
import turtle
from functools import total_ordering

@total_ordering
class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Provide radius or diameter")
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return math.pi * self.radius ** 2

    def __str__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter}, area={self.area:.2f})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

def draw_circles(circles):
    t = turtle.Turtle()
    t.speed(1)
    t.penup()
    x = -200
    for circle in circles:
        t.goto(x, 0)
        t.pendown()
        t.circle(circle.radius)
        t.penup()
        x += circle.diameter + 20
    turtle.done()

c1 = Circle(radius=5)
c2 = Circle(diameter=14)
c3 = c1 + c2
circles = [c1, c2, c3]
circles.sort()
draw_circles(circles)
