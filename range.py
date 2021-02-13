class MyRange:
    def __init__(self, *args):
        if len(args) == 1:
            self.stop = args[0]
            self.step = 1
            self.start = 0 - self.step
        elif len(args) == 2:
            self.step = 1
            self.start = args[0] - self.step
            self.stop = args[1]
        elif len(args) == 3:
            self.step = args[2]
            self.start = args[0] - self.step
            self.stop = args[1]
        else:
            raise IndexError('args takes only three arguments')

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            self.start += self.step
            if self.start < self.stop:
                return self.start
            else:
                raise StopIteration
        elif self.step < 0:
            self.start += self.step
            if self.start > self.stop:
                return self.start
            else:
                raise StopIteration
        else:
            raise ValueError('step should not be zero')


for i in MyRange(23, 57, 4):
    print(i)

