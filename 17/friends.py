from itertools import combinations, chain, permutations


# Write a function called friends_teams that takes a list of friends, a team_size (type int, default=2)
# and order_does_matter (type bool, default False).
def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return permutations(friends, team_size)
    else:
        return combinations(friends, team_size)
