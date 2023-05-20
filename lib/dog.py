#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        self.name = name
        self.breed = breed

max = Dog("Max", "Labrador")
print(max.name) 
print(max.breed) 

bella = Dog("Bella")
print(bella.name)
print(bella.breed)

