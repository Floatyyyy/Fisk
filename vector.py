import math

class Vector:
    def __init__(self, x=3, y=4):
        self.x = x
        self.y = y

    def length(self):
        # Længden af vektoren
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self):
        # Normaliserer vektoren (gør dens længde 1)
        length = self.length()
        if length != 0:
            return Vector(self.x / length, self.y / length)
        else:
            return Vector(0, 0)  # Undgår division med nul

    def dot(self, u):
        # Prikprodukt mellem to vektorer
        return self.x * u.x + self.y * u.y

    def __add__(self, u):
        # Addition af to vektorer
        return Vector(self.x + u.x, self.y + u.y)

    def __sub__(self, u):
        # Subtraktion af to vektorer
        return Vector(self.x - u.x, self.y - u.y)

    def scale(self, k):
        # Skalering af vektoren med en konstant
        return Vector(k * self.x, k * self.y)

    def __eq__(self, u):
        # Sammenligning af to vektorer
        return self.x == u.x and self.y == u.y

    def magnitude(self):
        # Længden af vektoren uden brug af __len__
        return self.length()

    def __str__(self):
        # Lavet om til streng for pæn udskrivning
        return f"({self.x}, {self.y})"

# Eksempel på brug:
v1 = Vector(3, 4)
v2 = Vector(4, 5)

print(v1.magnitude())  # Udskriv længden af v1
print(v1.normalize())  # Udskriv normaliseret v1
print(v1.dot(v2))
print(v1 + v2)
print(v1 - v2)
print(v1.scale(2))
print(v1 == Vector(3, 4))
