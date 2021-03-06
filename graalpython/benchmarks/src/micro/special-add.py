# special method __add__ dispatch
import time


class Num(object):
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return Num(self.n + other.n)

    def __repr__(self):
        return repr(self.n)


def do_compute(num):
    for i in range(num):
        sum_ = Num(0)
        one = Num(1)
        j = 0
        while j < num:
            sum_ = sum_ + one

            if sum_.n % 5 == 0:
                one.n = sum_.n % 3

            j += 1

    return sum_


def measure(num):
    print("Start timing...")
    start = time.time()

    for run in range(num):
        sum_ = do_compute(5000)  # 10000

    print("sum", sum_)

    duration = "%.3f\n" % (time.time() - start)
    print("special-add: " + duration)


print('warming up ...')
for run in range(2000):
    do_compute(5)  # 1000

measure(5)
