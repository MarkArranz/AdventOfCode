from typing import List


sum_of_priorities = 0

with open('./input.txt', 'r') as file:
    while (line := file.readline()) != '':
        half = len(line) // 2

        shared = set(line[:half]) & set(line[half:])
        item_type = shared.pop()

        if item_type.islower():
            sum_of_priorities += 1 + \
                bytes(item_type, 'ascii')[0] - bytes('a', 'ascii')[0]
        else: # item_type.isupper() == True
            sum_of_priorities += 27 + \
                bytes(item_type, 'ascii')[0] - bytes('A', 'ascii')[0]

print(sum_of_priorities)
