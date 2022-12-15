from enum import IntEnum
from typing import Dict, Literal, Tuple, cast


class ShapeType(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


ShapeValue = Literal[
    ShapeType.ROCK,
    ShapeType.PAPER,
    ShapeType.SCISSORS
]

P1_SHAPES: Dict[str, ShapeValue] = {
    'A': ShapeType.ROCK,
    'B': ShapeType.PAPER,
    'C': ShapeType.SCISSORS
}

P2_SHAPES: Dict[str, ShapeValue] = {
    'X': ShapeType.ROCK,
    'Y': ShapeType.PAPER,
    'Z': ShapeType.SCISSORS
}

P1_WIN_CONDITIONS = [
    (ShapeType.ROCK, ShapeType.SCISSORS),
    (ShapeType.PAPER, ShapeType.ROCK),
    (ShapeType.SCISSORS, ShapeType.PAPER)
]


class OutcomeType(IntEnum):
    LOSE = 0
    TIE = 3
    WIN = 6

OutcomeValue = Literal[OutcomeType.LOSE, OutcomeType.TIE, OutcomeType.WIN]

DESIRED_OUTCOME: Dict[str, OutcomeValue] = {
    'X': OutcomeType.LOSE,
    'Y': OutcomeType.TIE,
    'Z': OutcomeType.WIN
}


def get_p2_shape(p1_shape: ShapeValue, desired_outcome: OutcomeValue) -> ShapeValue:
    if desired_outcome == OutcomeType.TIE:
        return p1_shape
    
    if desired_outcome == OutcomeType.LOSE:
        match p1_shape:
            case ShapeType.ROCK:
                return ShapeType.SCISSORS
            case ShapeType.PAPER:
                return ShapeType.ROCK
            case ShapeType.SCISSORS:
                return ShapeType.PAPER
    
    # desired_outcome == OutcomeType.WIN
    match p1_shape:
        case ShapeType.ROCK:
            return ShapeType.PAPER
        case ShapeType.PAPER:
            return ShapeType.SCISSORS
        case ShapeType.SCISSORS:
            return ShapeType.ROCK


def play_round(
    p1_shape: ShapeValue,
    p2_shape: ShapeValue
) -> Tuple[int, int]:

        p1_score: int = p1_shape
        p2_score: int = p2_shape

        if p1_shape == p2_shape:
            p1_score += OutcomeType.TIE
            p2_score += OutcomeType.TIE
        elif (p1_shape, p2_shape) in P1_WIN_CONDITIONS:
            p1_score += OutcomeType.WIN
            p2_score += OutcomeType.LOSE
        else:
            p1_score += OutcomeType.LOSE
            p2_score += OutcomeType.WIN

        return (p1_score, p2_score)

def main() -> None:
    p1_total_score = 0
    p2_total_score = 0

    with open('./2022/02/input.txt', 'r') as file:
        while (line := file.readline()) != '':
            # Part 2 Code:
            p1_choice, outcome_code = line.split()

            desired_outcome = DESIRED_OUTCOME[outcome_code]

            p1_shape = P1_SHAPES[p1_choice]
            p2_shape = get_p2_shape(p1_shape, desired_outcome)

            p1_score, p2_score = play_round(p1_shape, p2_shape)

            p1_total_score += p1_score
            p2_total_score += p2_score

            # PART 1 Code:
            # p1_choice, p2_choice = line.split()
            # p1_score, p2_score = play_round(
            #     P1_SHAPES[p1_choice],
            #     P2_SHAPES[p2_choice])
            # p1_total_score += p1_score
            # p2_total_score += p2_score

    print(p2_total_score)

if __name__ == '__main__':
    main()
