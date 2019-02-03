def cashback(monthly_expenses):
    """

    >>> cashback(10_000)
    300.0
    """
    percent = 3
    result = percent * monthly_expenses / 100
    return result


def bmi(weight, height):
    """

    >>> bmi(106, 1.68) # doctest: +ELLIPSIS
    37.55...
    """
    result = weight / (height ** 2)
    return result
