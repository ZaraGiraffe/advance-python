from time import time, sleep


class DecorTimeCrit:
    def __init__(self, critical_time):
        self.critical_time = critical_time

    def benchmark(self, method):
        def helper(*args, **kwargs):
            time_start = time()
            res = method(*args, **kwargs)
            res_time = time() - time_start

            if res_time > self.critical_time:
                print(f'WARNING! {method.__name__} slow. Time = {res_time} sec.')

            return res

        return helper

    def __call__(self1, cls):
        class Helper:
            def __init__(self, *args, **kwargs):
                self.__obj = cls(*args, **kwargs)
                self.critical_time = self1.critical_time
                print(self1.critical_time)

            def __getattribute__(self, item):
                try:
                    is_my_attr = super().__getattribute__(item)
                except AttributeError:
                    pass
                else:
                    return is_my_attr

                attr = self.__obj.__getattribute__(item)

                if callable(attr):
                    return self1.benchmark(attr)
                else:
                    return attr

        return Helper





################################################################################


@DecorTimeCrit(critical_time=0.5)
class Test:
    def method_1(self):
        print('slow method start')
        sleep(1)
        print('slow method finish')

    def method_2(self):
        print('fast method start')
        sleep(0.1)
        print('fast method finish')


################################################################################


t = Test()
t.method_1()
t.method_2()

