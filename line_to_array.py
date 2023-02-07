def line_to_array(x: list, n):
    j=list()
    for i in [i*n for i in range(0,n)]:
        j.append(x[i:i+n])
    return j
