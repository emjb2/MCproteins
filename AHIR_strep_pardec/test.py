

def test(n):
    positions = list(range(n**2))
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            positions.remove((2*i+1)*n + (2*j+1))

    strep_only = positions.copy()
    for i in range(int(n/2)):
        for j in range(int(n/2)):
            strep_only.remove(2*i*n + 2*j)

    both = [x for x in positions if not x in strep_only]

    return [positions, strep_only, both]

