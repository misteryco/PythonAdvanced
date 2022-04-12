class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return self.diameter * self.__pi

    def calculate_area(self):
        return self.__pi * (self.diameter * 0.5)**2

    def calculate_area_of_sector(self, angle):
        # return (self.__pi * (self.diameter * 0.5)**2 / 360) * angle
        return (self.__pi * (self.diameter * 0.5) ** 2 / 360) * angle


diameter = int(input())
angle = int(input())
my_circle = Circle(diameter)

print(f"{my_circle.calculate_circumference():.2f}")
print(f"{my_circle.calculate_area():.2f}")
print(f"{my_circle.calculate_area_of_sector(angle):.2f}")


