from time import sleep
from datetime import datetime
class TrafficLight:
    _states = {'красный': 7, 'желтый': 2, 'зеленый': 10}
    _color = ''

    def running(self):
        for color, sw_time in self._states.items():
            self._color = color
            start_time = datetime.now()
            print(f"светофор переключился на '{self._color}' цвет " f'на {sw_time} секунд')
            sleep(sw_time)

            print(f"светофор переключится c '{self._color}' после "
                  f"{(datetime.now() - start_time).seconds} секунд")


t_lights = TrafficLight()
t_lights.running()