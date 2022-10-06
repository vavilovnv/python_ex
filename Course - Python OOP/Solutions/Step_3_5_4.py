# Условие задачи https://stepik.org/lesson/701990/step/4?unit=702091

class Track:

    def __init__(self, start_x=0, start_y=0):
        self.start_x = start_x
        self.start_y = start_y
        self.__track = []

    def add_track(self, tr):
        self.__track.append(tr)

    def get_tracks(self):
        return tuple(self.__track)

    def __len__(self):
        length, x0, y0 = 0, self.start_x, self.start_y
        for tr in self.__track:
            x1, y1 = tr.to_x, tr.to_y
            length += ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
            x0, y0 = x1, y1
        return int(length)

    def __eq__(self, other):
        return self.__len__() == other.__len__()

    def __gt__(self, other):
        return self.__len__() > other.__len__()

    def __lt__(self, other):
        return self.__len__() < other.__len__()


class TrackLine:

    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed


track1, track2 = Track(0, 0), Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
res_eq = track1 == track2
