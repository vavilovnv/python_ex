# Условие задачи https://stepik.org/lesson/804638/step/13

"""
Классы Lecture и Conference🌶️🌶️

1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании
экземпляра класс должен принимать три аргумента в следующем порядке:
- topic — тема выступления
- start_time — время начала выступления в виде строки в формате HH:MM
- duration — длительность выступления в виде строки в формате HH:MM

2. Также реализуйте класс Conference, описывающий конференцию, протяженностью
в один день. Конференция представляет собой набор последовательных
выступлений. При создании экземпляра класс не должен принимать никаких
аргументов.

Класс Conference должен иметь четыре метода экземпляра:
- add() — метод, принимающий в качестве аргумента выступление и добавляющий
его в конференцию. Если выступление пересекается по времени с другими
выступлениями, должно быть возбуждено исключение ValueError с текстом:
Провести выступление в это время невозможно
- total() — метод, возвращающий суммарную длительность всех выступлений в
конференции в виде строки в формате HH:MM
- longest_lecture() — метод, возвращающий длительность самого долгого
выступления в конференции в виде строки в формате HH:MM
- longest_break() — метод, возвращающий длительность самого долгого перерыва
между выступлениями в конференции в виде строке в формате HH:MM

Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами,
одно выступление может заканчиваться, например, в 12:00, а другое начинаться
в 12:00.

Примечание 2. Дополнительная проверка данных на корректность не требуется.
Гарантируется, что реализованные классы используются только с корректными
данными.

Примечание 3. Никаких ограничений касательно реализаций классов нет, они
могут быть произвольными.
"""

from datetime import datetime, time, timedelta
from functools import lru_cache

class Lecture:

    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration

class Conference:

    _PATTERN = "%H:%M"

    def __init__(self):
        self.confs = []

    @staticmethod
    @lru_cache
    def _convert_to_timestamp(start, end):
        sad_date️ = datetime(year=2022, month=2, day=24)
        t1 = sad_date️ + timedelta(hours=start.hour) + timedelta(minutes=start.minute)
        t2 = t1 + timedelta(hours=end.hour) + timedelta(minutes=end.minute)
        return t1.timestamp(), t2.timestamp()

    def _get_timestamps(self):
        return [
                self._convert_to_timestamp(
                    start=datetime.strptime(conf.start_time, self._PATTERN),
                    end=datetime.strptime(conf.duration, self._PATTERN)
                )
                for conf in self.confs
            ]

    def add(self, obj):
        if self.confs:
            temp = self._get_timestamps()
            temp.append(
                self._convert_to_timestamp(
                    start=datetime.strptime(obj.start_time, self._PATTERN),
                    end=datetime.strptime(obj.duration, self._PATTERN)
                )
            )
            temp.sort(key=lambda x: x[0])
            for i in range(1, len(temp)):
                if temp[i-1][1] > temp[i][0]:
                    raise ValueError("Провести выступление в это время невозможно")
        self.confs.append(obj)

    def total(self):
        temp = self._get_timestamps()
        sec = sum(int(conf[1] - conf[0]) for conf in temp)
        return time(hour=sec // 3600, minute=(sec % 3600) // 60).strftime(self._PATTERN)

    def longest_lecture(self):
        temp = self._get_timestamps()
        lecture = max(temp, key=lambda x: x[1] - x[0])
        sec = int(lecture[1] - lecture[0])
        return time(hour=sec // 3600, minute=(sec % 3600) // 60).strftime(self._PATTERN)

    def longest_break(self):
        temp = self._get_timestamps()
        temp.sort()
        sec = max([int(temp[i][0] - temp[i - 1][1]) for i in range(1, len(temp))])
        return time(hour=sec // 3600, minute=(sec % 3600) // 60).strftime(self._PATTERN)
