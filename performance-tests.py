import numpy
import timeit

arr = numpy.random.randint(-100, 100, 10000)
a = numpy.random.rand(1000, 1000)
b = numpy.random.rand(1000, 1000)


def sort_perf_test():
    numpy.sort(arr)


def dot_perf_test():
    numpy.dot(a, b)


if __name__ == '__main__':
    n = 100

    sort_time = timeit.timeit(sort_perf_test, number=n)
    print("[Array sorting] Time to complete " + str(n) + " iterations: ", sort_time, "seconds")

    dot_time = timeit.timeit(dot_perf_test, number=n)
    print("[Dot product] Time to complete " + str(n) + " iterations: ", dot_time, "seconds")