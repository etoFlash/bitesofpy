def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    my_cities = set(my_cities)
    other_cities = set(other_cities)
    return len(
        (my_cities | other_cities) - (my_cities & other_cities)
    )
