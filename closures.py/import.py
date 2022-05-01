# import decorator
import time


class Averager():

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)


avg = Averager()
print(avg(10))
print(avg(11))
print(avg(12))


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


avg = make_averager()
print(avg(10))
print(avg(11))
print(avg(12))

avg.__code__.co_varnames
avg.__code__.co_freevars
print(make_averager.__annotations__)
