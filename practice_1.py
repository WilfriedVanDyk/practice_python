""" practice page 2: OOP !!"""

class Car:
    def __init__(self, color, speed=0):
        self.color = color
        self.speed = speed
    def accelerate(self, mph):
        self.speed += mph




"""make a dog class and use inheretance"""
class Dog:
    """making a concrete dog
    """
    def __init__(self, name_of_dog):
        self.name = name_of_dog

"""factory pattern"""

