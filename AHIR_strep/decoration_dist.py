

def decoration_dist():
    # there'S space here to define some weird entropy distributions
    # the return is densities of partial decoration from AHIR with 0 to 6 strep attachments
    # the final number is pure strep.



    # Here we assume that we initially have 50:50 strep and AHIR
    # We then let the strep decorate the AHIR and note that it will run out p quickly
    return[15/36, 1/36, 1/36, 1/36, 1/36, 1/36, 1/36, 0]