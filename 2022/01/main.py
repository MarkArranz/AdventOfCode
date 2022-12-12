max_calories = 0
cur_calories = 0
with open('./input.txt', 'r') as file:
    while (line := file.readline()) != '':
        if line == '\n':
            max_calories = max(max_calories, cur_calories)
            cur_calories = 0
        else:
            cur_calories += int(line.rstrip())
print(max(max_calories, cur_calories))
