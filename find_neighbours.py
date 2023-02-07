from dirac_delta import dirac_delta


def find_neighbours(n, loc):
    # order is right, left, down, up
    return [loc + (dirac_delta(n - 1, loc % n) * (-n)) + 1,
            loc + ((dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n ** 2), (loc - n) % (n ** 2)]