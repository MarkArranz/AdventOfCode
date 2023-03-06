def count_full_overlap():
    full_overlap = 0
    with open("./input.txt") as f:
        for l in f:
            # Create two separate sets.
            pair = l.split(",")
            sets = []
            for sections in pair:
                sec_set = set()
                start, end = sections.split("-")
                s, e = int(start), int(end)
                while s <= e:
                    sec_set.add(s)
                    s += 1
                sets.append(sec_set)

            # Compare sets
            if sets[0].issubset(sets[1]) or sets[0].issuperset(sets[1]):
                full_overlap += 1
    print(full_overlap)

def count_any_overlap():
    any_overlap = 0
    with open("./input.txt") as f:
        for l in f:
            # Create two separate sets.
            pair = l.split(",")
            sets = []
            for sections in pair:
                sec_set = set()
                start, end = sections.split("-")
                s, e = int(start), int(end)
                while s <= e:
                    sec_set.add(s)
                    s += 1
                sets.append(sec_set)

            # Compare sets
            intersection =  sets[0] & sets[1]
            if len(intersection):
                any_overlap += 1
    print(any_overlap)


if __name__ == "__main__":
    count_any_overlap()
