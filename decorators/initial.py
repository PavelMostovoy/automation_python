from functools import reduce


def sum_numb(start: int, end: int) -> int:
    """
    Function return sum of numbers from start to end
    :param start:  int
    :param end:  end
    """
    var = 0
    for i in range(start, end + 1):
        var += i

    return var


def sum_numb_1(start: int, end: int):
    data = [x for x in range(start, end + 1)]

    return sum(data)


def sum_numb_2(start: int, end: int):
    result = reduce(lambda x, y: x + y, range(start, end + 1))
    return result


def sum_numb_0(start: int, end: int):
    h = end + 1
    l = h - start
    result = (h * l) / 2
    return int(result)


if __name__ == "__main__":
    print(sum_numb_0(1, 100))

    print(sum_numb(1, 100))

    print(__name__)
