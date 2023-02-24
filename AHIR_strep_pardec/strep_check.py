from general_functions.find_neighbours import find_neighbours


def strep_check(n, positions, strep_only, heights):
    for i in strep_only:
        current_height = heights[i]
        neighbours = [x for x in find_neighbours(n, i) if x in positions]
        neighbours_heights = [heights[x] for x in neighbours]

        neighbours_count = [1 for x in neighbours if heights[x] >= current_height]
        if not neighbours_count:
            heights[i] == (max(neighbours_heights)+1)//2 + 1
            print("PROBLEM")

    return heights
