from typing import Set, Tuple


def add(t1: Tuple, t2: Tuple) -> Tuple:
    return (t1[0] + t2[0], t1[1] + t2[1])


def subtract(t1: Tuple, t2: Tuple) -> Tuple:
    return (t1[0] - t2[0], t1[1] - t2[1])


def sign(t: Tuple) -> Tuple:
    return (t[0] / abs(t[0]) if t[0] else 0, t[1] / abs(t[1]) if t[1] else 0)


def main(num_knots: int):
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    rope = [(0, 0)] * num_knots

    move_map = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),
    }

    tail_positions: Set[Tuple[int, int]] = set()
    tail_positions.add(rope[-1])

    for line in lines:
        direction, distance = line.split()
        h_move = move_map[direction]
        for _ in range(int(distance)):
            rope[0] = add(rope[0], h_move)
            prev = rope[0]
            for i in range(1, num_knots):
                diff = subtract(prev, rope[i])

                if abs(diff[0]) == 2 or abs(diff[1]) == 2:  # a move is required
                    move = sign(diff)
                    rope[i] = add(rope[i], move)
                    prev = rope[i]
                else:
                    break
            tail_positions.add(rope[-1])

    print("Positions tail visited at least once:")
    print(len(tail_positions))


if "__main__" == __name__:
    import sys

    try:
        num_knots = int(sys.argv[1])
    except IndexError:
        num_knots = 2

    main(num_knots)
