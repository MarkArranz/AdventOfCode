from collections import deque


def find_start_of_packet_marker():
    with open("./input.txt") as f:
        stream = f.readline()
    unique_needed = 14
    marker = deque(maxlen=unique_needed)
    for count, char in enumerate(stream, 1):
        while char in marker:
            marker.popleft()
        marker.append(char)
        if len(marker) == unique_needed:
            return count
    raise Exception('No valid marker found.')



print(find_start_of_packet_marker())
