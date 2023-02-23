# tells us if attachemtn at the given stack is possible (eg it is not possible if a strep has no AHIR next to it)

def is_attachment_possible(n, loc, heights, strep_only):
    # 0 is no, 1 is yes
    if loc in strep_only:
        if heights[loc]%2 == 1:
            return 0
        else:
            return 1
    else:
        return 1
