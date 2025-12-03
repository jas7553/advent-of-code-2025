import pathlib
from typing import Iterable

BASE_DIR = pathlib.Path(__file__).parent


def read_input() -> Iterable[str]:
    with open(BASE_DIR / "input.txt", "r") as f:
        for line in f.readlines():
            yield line.strip()


def find_largest_joltage(bank: str) -> int:
    batteries = list(map(int, bank))

    left_battery = batteries[-2]
    left_index = len(batteries) - 1
    for i in range(len(batteries) - 2, -1, -1):
        if batteries[i] > left_battery:
            left_battery = batteries[i]
            left_index = i
        elif batteries[i] == left_battery:
            left_index = i

    right_battery = batteries[-1]
    for i in range(len(batteries) - 1, left_index, -1):
        if batteries[i] > right_battery:
            right_battery = batteries[i]

    return int(str(left_battery) + str(right_battery))


def part1() -> None:
    solution = sum(
        find_largest_joltage(bank)
        for bank in read_input()
    )

    print(solution)


def part2() -> None:
    pass


if __name__ == "__main__":
    part1()
    part2()
