def div_zero_error(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return 0
