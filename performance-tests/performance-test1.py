import numpy as np
import timeit

a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)


def built_in_dot():
    a @ b


def numpy_dot():
    np.dot(a, b)


if __name__ == '__main__':
    n = 1000

    print("Using Python's '@' operator to calculate dot product", n, "times.")
    dot_time = timeit.timeit(built_in_dot, number=n)
    print("Time to complete " + str(n) + " iterations:", dot_time, "seconds")
    print("Average time to complete 1 iteration:", dot_time / n, "seconds")

    print("-----------------------------------------------------")

    print("Using NumPy to calculate dot product", n, "times.")
    dot_time = timeit.timeit(numpy_dot, number=n)
    print("Time to complete " + str(n) + " iterations:", dot_time, "seconds")
    print("Average time to complete 1 iteration:", dot_time / n, "seconds")
