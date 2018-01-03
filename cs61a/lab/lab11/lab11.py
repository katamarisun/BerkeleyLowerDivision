def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1

def trap(s, k):
    """Return a generator that yields the first K values in iterable S,
    but raises a ValueError exception if any more values are requested.

    >>> t = trap([3, 2, 1], 2)
    >>> next(t)
    3
    >>> next(t)
    2
    >>> next(t)
    ValueError
    >>> list(trap(range(5), 5))
    ValueError
    """
    assert len(s) >= k
    count = 0
    while count < k:
        yield s[count]
        count += 1
    raise ValueError

def repeated(t, k):
    """Return the first value in iterable T that appears K times in a row.

    >>> s = [3, 2, 1, 2, 1, 4, 4, 5, 5, 5]
    >>> repeated(trap(s, 7), 2)
    4
    >>> repeated(trap(s, 10), 3)
    5
    >>> print(repeated([4, None, None, None], 3))
    None
    """
    assert k > 1
    track = [0]
    tracker = iter(t)
    while len(track) < k:
        x = next(tracker)
        if track[0] == x:
            track.append(x)
        else:
            track = [x]
    return track[0]
    "*** YOUR CODE HERE ***"

def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    yield n
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        yield n

