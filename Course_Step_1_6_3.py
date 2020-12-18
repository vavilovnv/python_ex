# условие задачи https://stepik.org/lesson/24462/step/9?auth=login&unit=6768

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, item):
        self.log(item)
        # вызов метода append() предка list возможен тремя способами
        # super().append(item)
        # super(LoggableList, self).append(item)
        list.append(self, item)

sp = LoggableList()
sp.append(1)
print(sp)