def get_others(map_, r, c):
    """Go through the map and check the size of the island
       (= summing up all the 1s that are part of the island)

       Input - the map, row, column position
       Output - return the total numbe)
    """
    nums = 0
    for x, y in ((-1, 0), (0, -1), (1, 0), (0, 1)):
        try:
            if r + x < 0 or c + y < 0:
                continue
            if map_[r + x][c + y] == 1:
                nums += 1
        except IndexError:
            pass

    return nums


def island_size(map_):
    """Hint: use the get_others helper

    Input: the map
    Output: the perimeter of the island
    """
    perimeter = 0
    row_len = len(map_[0])
    for x in range(row_len):
        for y in range(row_len):
            if map_[x][y] == 1:
                perimeter += (4 - get_others(map_, x, y))

    return perimeter
