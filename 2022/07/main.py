from __future__ import annotations
from enum import StrEnum, auto
from functools import reduce
import operator as op
from typing import Callable, List


class NodeType(StrEnum):
    DIR = auto()
    FILE = auto()


class Root:
    def __init__(self) -> None:
        self.name: str = "/"
        self.size: int = 0
        self.children: List[Node] = []

    def __repr__(self) -> str:
        return f"Root / {self.size}"


class Node:
    def __init__(
        self, name: str, type: NodeType, parent: Root | Node, size: int = 0
    ) -> None:
        self.name = name
        self.type = type
        self.parent = parent
        self.size = size
        self.children: List[Node] = []

    def __repr__(self) -> str:
        return f"{self.type} {self.name} {self.size}"


def build_filesystem(lines: List[str]) -> Root:
    root = Root()
    current: Root | Node = root
    for line in lines:
        match (line.split()):
            case ["$", "cd", "/"]:
                current = root
                continue
            case ["$", "cd", ".."]:
                current = current.parent if isinstance(current, Node) else root
            case ["$", "cd", name]:
                current, *_ = [
                    child for child in current.children if child.name == name
                ]
            case ["$", "ls"]:
                continue
            case ["dir", name]:
                current.children.append(Node(name, NodeType.DIR, current))
            case [size, name]:
                current.children.append(
                    Node(name, NodeType.FILE, current, int(size)))
            case any:
                Exception(f"Unmatched pattern: {any}")
    return root


def get_size(node: Root | Node) -> int:
    for child in node.children:
        if child.type == NodeType.DIR:
            node.size += get_size(child)
        else:
            node.size += child.size
    return node.size


def filter_dirs_by_threshold(
    node: Root | Node, threshold: int, compare: Callable[[int, int], bool]
) -> List[Node]:
    filtered = []
    for child in node.children:
        if child.type == NodeType.DIR:
            filtered += filter_dirs_by_threshold(child, threshold, compare)
            if compare(child.size, threshold):
                filtered.append(child)
    return filtered


def main():
    with open("input.txt", "r") as f:
        lines = f.readlines()

    root = build_filesystem(lines)
    file_system_size = get_size(root)

    # region Part 1
    # Find qualifying nodes
    threshold = 100_000
    filtered = filter_dirs_by_threshold(root, threshold, op.le)
    sum = reduce(lambda acc, n: acc + n.size, filtered, 0)
    print(f"Sum: {sum}")
    # endregion

    # region Part 2
    disk_capacity = 70_000_000
    used_space = file_system_size
    free_space = disk_capacity - used_space

    free_space_required = 30_000_000
    extra_space_needed = free_space_required - free_space

    filtered = filter_dirs_by_threshold(root, extra_space_needed, op.ge)
    filtered.sort(key=lambda n: n.size)
    print(f"Directory Size: {filtered[0].size}")
    # endregion


if "__main__" == __name__:
    main()
