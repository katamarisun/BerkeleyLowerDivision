def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    >>> x = []
    >>> for i in range(100):
    ...     x = [x] + [i]       # very deep list
    ...
    >>> deep_len(x)
    100
    """
    return sum([deep_len(lst[i]) if isinstance(lst[i], list) else 1 for i in range(len(lst))])
