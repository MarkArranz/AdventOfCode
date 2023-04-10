from typing import Set, Tuple


class TreeGrid:
    def __init__(self, rows: int, cols: int):
        self._last_row = rows - 1
        self._last_col = cols - 1

        self._by_row = [[0 for _ in range(cols)] for _ in range(rows)]
        self._by_col = [[0 for _ in range(rows)] for _ in range(cols)]

        self._visible: Set[Tuple[int, int]] = set()

    def add(self, height: int, row: int, col: int) -> None:
        self._by_row[row][col] = height
        self._by_col[col][row] = height
        # Trees in the first row, last row, first column, or last column
        # are automatically visible.
        if row == 0 or row == self._last_row or col == 0 or col == self._last_col:
            self._visible.add((row, col))

    def get_visible_count(self) -> int:
        self._evaluate_visibility()
        return len(self._visible)

    def _evaluate_visibility(self) -> None:
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

    def get_best_scenic_score(self) -> int:
        high_score = 0
        for r in range(len(self._by_row)):
            for c in range(len(self._by_col)):


def main():
    lines = []
    with open("input.txt", "r") as f:
        lines = f.readlines()

    total_rows = len(lines)
    total_col = len(lines[0].strip())

    g = TreeGrid(total_rows, total_col)
    for r, line in enumerate(lines):
        for c, height in enumerate(line.strip()):
            g.add(int(height), r, c)

    print(f'Visible Trees: {g.get_visible_count()}')


if '__main__' == __name__:
    main()
