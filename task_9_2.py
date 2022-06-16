class Road():
    _lenght = None
    _widht = None
    massa = None
    thickness = None
    def __init__(self, lenght, widht):
        self._lenght = lenght
        self._widht = widht
        print('дорога до обьекта')

    def calculation(self):
        self.massa = 25
        self.thickness = 5
        calc = self._lenght * self._widht * self.massa * self.thickness / 1000
        print(f'нужно {calc} тонн асфальта для строительства дороги')
road_to_object = Road(5000, 20)
road_to_object.calculation()
