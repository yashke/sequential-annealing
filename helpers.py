from math import sqrt

def triangularize(collection):
    """
    >>> triangularize([1, 2, 3, 4, 5, 6, 7])
    [[1, 2, 3], [4, 5, 6], [7]]
    """
    result = []
    i = 0
    for item in collection:
        if i % 3 == 0:
            result.append([item])
        else:
            result[-1].append(item)
        i += 1
    return result


def length(x, y):
    """
    >>> length((0.0, 0.0), (1.0, 0.0))
    1.0
    >>> length((0.0, 1.0), (0.0, 0.0))
    1.0
    >>> length((0.0, 1.0), (2.0, 1.0))
    2.0
    """
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)

def length_from(points, start):
    """
    >>> length_from([(1.0,1.0), (2.0,1.0), (3.0,1.0)], (0.0,1.0))
    6.0
    """
    result = .0
    old = start
    for point in points:
        result += length(old, point)
        old = point
    result += length(old, start)
    return result


def cost(solution, start):
    result = .0
    for triangle in solution:
        result += length_from(triangle, start)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
