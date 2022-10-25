# Условие задачи https://stepik.org/lesson/701998/step/9?unit=702099

class Aircraft:

    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, name, value):
        if name == '_model' and not isinstance(value, str):
            raise TypeError('неверный тип аргумента')
        if (name in ('_mass', '_speed', '_top')
                and not (isinstance(value, (int, float)) and value > 0)):
            raise TypeError('неверный тип аргумента')
        super.__setattr__(self, name, value)


class PassengerAircraft(Aircraft):

    def __init__(self, model, mass, speed, top, chairs):
        super(PassengerAircraft, self).__init__(model, mass, speed, top)
        self._chairs = chairs

    def __setattr__(self, name, value):
        if (name == '_chairs'
                and not (isinstance(value, int) and value > 0)):
            raise TypeError('неверный тип аргумента')
        super(PassengerAircraft, self).__setattr__(name, value)


class WarPlane(Aircraft):

    def __init__(self, model, mass, speed, top, weapons):
        super(WarPlane, self).__init__(model, mass, speed, top)
        self._weapons = weapons

    def __setattr__(self, name, value):
        if (name == '_weapons'
                and not isinstance(value, dict)):
            raise TypeError('неверный тип аргумента')
        super(WarPlane, self).__setattr__(name, value)


planes = [
    PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
    PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
    WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
    WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})
]
