


def whats_there_now(loc, heights, both):
    # 0 is strep, 1 is AHIR
    current_height = heights[loc][1]
    if loc in both:
        if current_height%2 == 0:
            return 0 
        else:
            return 1
    else:
        return 0
