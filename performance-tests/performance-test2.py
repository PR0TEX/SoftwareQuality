import numpy as np
import timeit

arr = np.random.randint(-10000, 10000, 1000000)


def numpy_sort():
    np.sort(arr)


def array_sort():
    arr.sort()


if __name__ == '__main__':
    n = 1000

    print("Using Python's built-in Array module to sort an array of 1000000 random elements", n, "times.")
    dot_time = timeit.timeit(array_sort, number=n)
    print("Time to complete", n, "iterations:", dot_time, "seconds")
    print("Average time to complete 1 iteration:", dot_time / n, "seconds")

    print("-----------------------------------------------------")

    print("Using NumPy to sort an array of 1000000 random elements", n, "times.")
    dot_time = timeit.timeit(numpy_sort, number=n)
    print("Time to complete", n, "iterations:", dot_time, "seconds")
    print("Average time to complete 1 iteration:", dot_time / n, "seconds")
