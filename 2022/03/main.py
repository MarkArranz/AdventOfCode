from functools import reduce
from io import TextIOWrapper
from typing import List, Set


def sum_shared_priorities(file: TextIOWrapper) -> int:
    sum_of_priorities = 0

    for line in file:
        half = len(line) // 2

        shared = set(line[:half]) & set(line[half:])
        item_type = shared.pop()

        if item_type.islower():
            sum_of_priorities += 1 + ord(item_type) - ord('a')
        else:  # item_type.isupper() == True
            sum_of_priorities += 27 + ord(item_type) - ord('A')

    return sum_of_priorities


def sum_badge_priorities(file: TextIOWrapper) -> int:
    badge_priority_sum: int = 0
    group: List[Set[str]] = []

    for line in file:
        group.append(set(line.rstrip()))

        if len(group) < 3:
            continue

        badge = reduce(lambda a, b: a & b, group).pop()

        if badge.islower():
            badge_priority_sum += 1 + ord(badge) - ord('a')
        else:  # item_type.isupper() == True
            badge_priority_sum += 27 + ord(badge) - ord('A')

        group.clear()

    return badge_priority_sum


def main():
    # Part 1
    with open('./2022/03/input.txt') as file:
        print(sum_shared_priorities(file))

    # Part 2
    with open('./2022/03/input.txt') as file:
        print(sum_badge_priorities(file))


if __name__ == '__main__':
    main()
