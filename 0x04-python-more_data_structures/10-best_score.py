#!/usr/bin/python3


def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    bet = list(a_dictionary.keys())[0]
    huge = a_dictionary[bet]
    for r, v in a_dictionary.items():
        if g > huge:
            huge = g
            bet = r
    return (bet)
