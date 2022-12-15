from typing import List

def adjust_max_calories(max_calories: List[int], cur_calories: int) -> None:
    for i, v in enumerate(max_calories):
        if (v < cur_calories):
            max_calories.insert(i, cur_calories)
            max_calories.pop()
            return
    return

max_size = int(input("Find the top __ Elves carrying the most Calories.\nEnter a number: "))

max_calories: List[int] = []
cur_calories = 0

with open('./2022/01/input.txt', 'r') as file:
    while (line := file.readline()) != '':
        if line != '\n':
            cur_calories += int(line.rstrip())
            continue

        if len(max_calories) < max_size:
            max_calories.append(cur_calories)
            cur_calories = 0
            continue

        adjust_max_calories(max_calories, cur_calories)
        cur_calories = 0


adjust_max_calories(max_calories, cur_calories)

print(sum(max_calories))
