import random

def adjacent_linear(randomize=false):
    """
    Return x and y offsets for adjacent moves in
    linear directions

                         #
                        #x#
                         #

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (int, int): List of x and y offsets from
        current position
    """
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves

def adjacent_octile(randomize=false):
    """
    Return x and y offsets for adjacent moves in
    octile directions

                        ###
                        #x#
                        ###

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (int, int): List of x and y offsets from
        current position
    """
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves

def bc19_4_radius(randomize=false):
    """
    Return x and y offsets for adjacent moves in
    four unit distance of the current position.

                         #
                        ###
                       ##x##
                        ###
                         #

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (int, int): List of x and y offsets from
        current position
    """
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (2, 0),
        (0, 2),
        (0, -2),
        (-2, 0)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves


def bc19_9_radius(randomize=false):
    """
    Return x and y offsets for adjacent moves in
    nine unit distance of the current position.

                         #
                        ###
                       #####
                      ###x###
                       #####
                        ###
                         #

    Args:
        randomize (boolean): randomize order of moves
            or not

    Returns:
        List (int, int): List of x and y offsets from
        current position
    """
    moves = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
        (2, 0),
        (0, 2),
        (0, -2),
        (-2, 0),
        (0, 3),
        (1, 2),
        (2, 1),
        (3, 0),
        (2, -1),
        (1, -2),
        (0, -3),
        (-1, -2),
        (-2, -1),
        (-3, 0),
        (-2, 1),
        (-1, 2),
        (2, 2),
        (2, -2),
        (-2, 2),
        (-2, -2)
    ]

    if randomize:
        return random.shuffle(moves)
    else:
        return moves
