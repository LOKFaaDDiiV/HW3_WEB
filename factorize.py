from multiprocessing import Process, cpu_count, Pool
from datetime import datetime
from time import sleep


def body(n):
    res = []
    for i in range(1, n + 1):
        if n % i == 0:
            res.append(i)
    return res


def factorize(*number):
    result = []
    for num in number:
        result.append(body(num))
    return result


def factorize_multi(*number):
    if cpu_count() < len(number):
        proc_num = cpu_count()
    else:
        proc_num = len(number)
    with Pool(processes=proc_num) as pool:
        return pool.map(body, number)


if __name__ == '__main__':
    start_time = datetime.now()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    time2 = datetime.now() - start_time

    start_time = datetime.now()
    e, f, g, h = factorize_multi(128, 255, 99999, 10651060)
    time1 = datetime.now() - start_time

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060]

    assert e == [1, 2, 4, 8, 16, 32, 64, 128]
    assert f == [1, 3, 5, 15, 17, 51, 85, 255]
    assert g == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert h == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
                 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212,
                 2662765, 5325530, 10651060]

    print(f"Multi = {time1}")
    print(f"Single = {time2}")
