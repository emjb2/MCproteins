import dirac_delta


def find_neighbours(n, loc):
    return [loc + (dirac_delta.dirac_delta(n - 1, loc % n) * (-n)) + 1,
            loc + ((dirac_delta.dirac_delta(0, loc % n)) * n) - 1,
            (loc + n) % (n ** 2), (loc - n) % (n ** 2)]
