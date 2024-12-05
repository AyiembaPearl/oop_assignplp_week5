# -*- coding: utf-8 -*-
class Car:
    def move(self):
        return "Driving"
class Plane:
    def move(self):
        return "Flying"
    
#polymorphism
for transportation in [Car(), Plane()]:
    print(transportation.move())