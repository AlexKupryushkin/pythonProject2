import time

class Auto:
    def __init__(self, brand, age, mark, color='red', weight=2000):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print('move')
    def stop(self):
        print('stop')
    def birthday(self):
        self.age += 1
    def __str__(self):
        return f"{self.brand} | {self.mark} | {self.age} "

auto1 = Auto('VW', 5, 'Polo')
print(auto1)
auto1.move()
auto1.birthday()
print(auto1)
auto1.move()
auto1.birthday()
print(auto1)

print('-' * 50)



class Truck(Auto):
    def __init__(self, max_load, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_load = max_load

    def move(self):
        print('attention')
        print ('move')
    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)


truck1 = Truck(7, 'VW', 5, 'Polo')
truck2 = Truck(11,'BMW', 10, 'xdrive')
#
print(truck1)
truck1.load()
truck1.move()
truck1.birthday()
print(truck1)
truck1.stop()
print(truck2)
truck2.load()
truck1.move()
truck2.birthday()
print(truck2)
truck2.stop()

print('-' * 50)

class Car(Auto):
    def __init__(self, max_speed, brand, age, mark):
        super().__init__(brand, age, mark)
        self.max_speed = max_speed

    def move(self):
        print('move')
        print(f'max_speed is {self.max_speed}')

car1 = Car(200, 'Niva', 10, '4x4')
print(car1)
car1.move()
car1.birthday()
print(car1)
car1.stop()

