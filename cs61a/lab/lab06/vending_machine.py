def vending_machine(snacks):
    """Cycles through list of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    index = 0
    def machine():
        nonlocal index
        if index < len(snacks):
            rv = snacks[index]
            index += 1
            return rv
        else:
            index = 0
            return snacks[index]
    return machine
