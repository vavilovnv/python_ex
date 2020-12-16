# https://stepik.org/lesson/24461/step/9?unit=6767

class Buffer:
    def __init__(self):
        self.sp = []

    def print_sum(self):
        if len(self.sp) >= 5:
            print(sum(self.sp[:5]))
            self.sp = self.sp[5:]
            if len(self.sp) >= 5:
                self.print_sum()

    def add(self, *a):
        self.sp += a
        self.print_sum()


    def get_current_part(self):
       return self.sp

buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part()