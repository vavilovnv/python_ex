# Условие задачи https://stepik.org/lesson/702001/step/7?unit=702102

class Planet:

    def __init__(self, name, diametr, period_solar, period):
        self._name = name
        self._diametr = diametr
        self._period_solar = period_solar
        self._period = period


class SolarSystem:

    __instance = None
    __slots__ = ('_mercury', '_venus', '_earth', '_mars',
                 '_jupiter', '_saturn', '_uranus', '_neptune')

    def __new__(cls, *args, **kwargs):
        cls.__instance = cls.__instance or super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self._mercury = Planet('Меркурий', 4878, 87.97, 1407.5)
        self._venus = Planet('Венера', 12104, 224.7, 5832.45)
        self._earth = Planet('Земля', 12756, 365.3, 23.93)
        self._mars = Planet('Марс', 6794, 687, 24.62)
        self._jupiter = Planet('Юпитер', 142800, 4330, 9.9)
        self._saturn = Planet('Сатурн', 120660, 10753, 10.63)
        self._uranus = Planet('Уран', 51118, 30665, 17.2)
        self._neptune = Planet('Нептун', 49528, 60150, 16.1)


s_system = SolarSystem()
