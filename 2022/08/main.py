from typing import Set, Tuple


class TreeGrid:
    def __init__(self, filename: str) -> None:
        with open("input.txt", "r") as f:
            lines = f.readlines()

        row_count = len(lines)
        col_count = len(lines[0].strip())

        self._last_row = row_count - 1
        self._last_col = col_count - 1

        self._by_row = [[0 for _ in range(col_count)]
                        for _ in range(row_count)]
        self._by_col = [[0 for _ in range(row_count)]
                        for _ in range(col_count)]

        self._visible: Set[Tuple[int, int]] = set()
        self._highest_scenic_score = -1

        for r, line in enumerate(lines):
            for c, height in enumerate(line.strip()):
                self._add(int(height), r, c)

        self._evaluate_grid()

    def _add(self, height: int, row: int, col: int) -> None:
        self._by_row[row][col] = height
        self._by_col[col][row] = height
        # Trees in the first row, last row, first column, or last column
        # are automatically visible.
        if row == 0 or row == self._last_row or col == 0 or col == self._last_col:
            self._visible.add((row, col))

    def get_visible_count(self) -> int:
        return len(self._visible)

    def _evaluate_grid(self) -> None:
        for r in range(1, self._last_row):
            for c in range(1, self._last_col):
                if self._is_visible_in_col(r, c) or self._is_visible_in_row(r, c):
                    self._visible.add((r, c))

    def _is_visible_in_col(self, row: int, col: int) -> bool:
        tree_column = self._by_col[col]
        current_tree = tree_column[row]

        trees_above = tree_column[:row]
        trees_below = tree_column[row+1:]

        can_see_from_top = not any(
            [True for tree_above in trees_above if tree_above >= current_tree])
        can_see_from_bottom = not any(
            [True for tree_below in trees_below if tree_below >= current_tree])

        return can_see_from_top or can_see_from_bottom

    def _is_visible_in_row(self, row: int, col: int) -> bool:
        tree_row = self._by_row[row]
        current_tree = tree_row[col]

        left_trees = tree_row[:col]
        right_trees = tree_row[col+1:]

        can_see_from_left = not any(
            [True for left_tree in left_trees if left_tree >= current_tree]
        )
        can_see_from_right = not any(
            [True for right_tree in right_trees if right_tree >= current_tree]
        )

        return can_see_from_left or can_see_from_right

    def get_highest_scenic_score(self) -> int:
        high_scenic_score = -1
        for r, c in self._visible:
            # All trees on the edge have a scenic score of 0
            if r == 0 or r == self._last_row or c == 0 or c == self._last_col:
                continue
            scenic_score = self._get_scenic_score(r, c)
            high_scenic_score = max(high_scenic_score, scenic_score)
        return high_scenic_score

    def _get_scenic_score(self, r: int, c: int) -> int:
        row = self._by_row[r]
        col = self._by_col[c]
        curr = row[c]

        to_left = row[c-1::-1]
        to_right = row[c+1:]
        upward = col[r-1::-1]
        downward = col[r+1:]
        directions = [to_left, to_right, upward, downward]

        total_score = 1
        score = 0
        for direction in directions:
            for tree in direction:
                score += 1
                if tree >= curr:
                    break
            total_score *= score
            score = 0

        return total_score


def main():
    g = TreeGrid("input.txt")
    print(f'Visible Trees: {g.get_visible_count()}')
    print(f'Highest scenic score: {g.get_highest_scenic_score()}')


if '__main__' == __name__:
    main()
