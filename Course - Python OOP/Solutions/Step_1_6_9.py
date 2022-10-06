# Условие задачи https://stepik.org/lesson/701976/step/9?unit=702077

TYPE_OS = 1 # 1 - Windows; 2 - Linux


class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(self, *args, **kwargs):
        obj = DialogWindows() if TYPE_OS == 1 else DialogLinux()
        setattr(obj, 'name', *args)
        return obj
