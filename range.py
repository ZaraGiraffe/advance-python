class My_range:
    def __init__(self, start: int, step: int, stop: int):
        self.start = start - step
        self.step = step
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start < self.stop:
            return self.start
        else:
            raise StopIteration


for i in My_range(3, 12, 66):
    print(i)

