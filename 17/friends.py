from itertools import combinations, chain, permutations


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return permutations(friends, team_size)
    else:
        return combinations(friends, team_size)
