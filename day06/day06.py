import pathlib
from math import prod
from typing import Generator


def read_input() -> list[str]:
    return (pathlib.Path(__file__).parent / "input.txt").read_text().splitlines()


def column_boundaries(lines: list[str]) -> Generator[tuple[int, int], None, None]:
    start_col, end_col = 0, 1
    while True:
        while not is_all_spaces(lines, end_col):
            end_col += 1

        yield start_col, end_col - 1

        start_col, end_col = end_col + 1, end_col + 2

        if start_col == len(lines[0]) + 1:
            break


def is_all_spaces(lines: list[str], col: int) -> bool:
    if col == len(lines[0]):
        return True

    return all([line[col] == ' ' for line in lines[0:-1]])


def part1() -> None:
    lines = [line.split() for line in read_input()]

    solution = 0
    for i, operator in enumerate(lines[-1]):
        operands = [int(operand[i]) for operand in lines[:-1]]
        if operator == '+':
            solution += sum(operands)
        elif operator == '*':
            solution += prod(operands)

    print(solution)


def part2() -> None:
    lines = read_input()

    solution = 0
    for col_start, col_end in column_boundaries(lines):
        operator = lines[-1][col_start]
        operands = [int("".join(operand)) for operand in
                    zip(*[list(row[col_start:col_end + 1]) for row in lines[:-1]])]
        if operator == '+':
            solution += sum(operands)
        elif operator == '*':
            solution += prod(operands)

    print(solution)


if __name__ == "__main__":
    part1()
    part2()
