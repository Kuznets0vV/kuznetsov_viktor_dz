class Car:
    speed = None
    color = None
    name = None
    is_police = False
    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return 'машина поехала'
    def stop(self):
        return 'машина остановилась'
    def turn(self):
        return 'машина повернула'
    def show_speed(self):
        return f'текущая скорость {self.speed}'
class TownCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)
    def show_speed(self, speed):
        if speed > 60:
            print('превышение скорости')
        else:
            print(f'текущая скорость {speed}')
class SportCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Car):
    def show_speed(self, speed):
        if speed > 40:
            print('превышение скорости')
class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)
ferrari = SportCar('Portofino', 200, 'Красный',)
print(ferrari.name, ferrari.color, ferrari.speed, ferrari.is_police)
print(ferrari.go(), ferrari.turn(), ferrari.stop())
wolkswagen = TownCar('golf', 50, 'white')
print(wolkswagen.show_speed(50))
ford = WorkCar('Transporter', 45, 'Black')
print(ford.name, ford.color, ford.speed, ford.show_speed(45))




