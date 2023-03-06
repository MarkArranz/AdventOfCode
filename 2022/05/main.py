def get_top_crates(crane_model_number: int) -> str:
    with open("./input.txt") as f:
        lines = f.readlines()

    stack_base_line = 7
    move_start_line = 10

    stacks = [[] for _ in range(9)]

    # create stacks from the bottom up
    for crate_level in lines[stack_base_line::-1]:
        stack_index = 0
        while crate_level:
            crate, crate_level = crate_level[:4], crate_level[4:]
            crate_content = crate.strip().strip("[]")
            if crate_content:
                stacks[stack_index].append(crate_content)
            stack_index += 1

    # simulate crane moves
    if crane_model_number == 9001:
        for line in lines[move_start_line:]:
            num_crates, start, end = [
                int(word) for word in line.split() if word.isdigit()
            ]
            s, e = start - 1, end - 1
            stacks[e] += stacks[s][-num_crates:]
            del stacks[s][-num_crates:]
    else:
        for line in lines[move_start_line:]:
            num_crates, start, end = [
                int(word) for word in line.split() if word.isdigit()
            ]
            for _ in range(num_crates):
                stacks[end - 1].append(stacks[start - 1].pop())

    # get top crate from each stack
    top_crates = [stack[-1] for stack in stacks]

    return "".join(top_crates)


print(get_top_crates(9001))
