import dataclasses
import pathlib
from typing import List

BASE_DIR = pathlib.Path(__file__).parent


@dataclasses.dataclass
class LargeGrid:
    rows: List[str]

    def __str__(self) -> str:
        return "\n".join(self.rows)

    def has_fewer_than_four_adjacent_rolls(self, row, col) -> bool:
        adjacent_count = 0
        for dx in (-1, 0, 1):
            if row + dx < 0 or row + dx >= len(self.rows):
                continue

            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                if col + dy < 0 or col + dy >= len(self.rows[row + dx]):
                    continue
                if self.rows[row + dx][col + dy] == '@':
                    adjacent_count += 1

                if adjacent_count >= 4:
                    return False

        return True


def read_input() -> LargeGrid:
    rows = (BASE_DIR / "input.txt").read_text().splitlines()

    return LargeGrid(rows)


def remove_rolls_of_paper(large_grid: LargeGrid) -> tuple[int, LargeGrid]:
    new_rows = []
    remove_count = 0
    for row in range(0, len(large_grid.rows)):
        new_row = []
        for col in range(0, len(large_grid.rows[row])):
            if large_grid.rows[row][col] == '@':
                if large_grid.has_fewer_than_four_adjacent_rolls(row, col):
                    new_row.append('x')
                    remove_count += 1
                else:
                    new_row.append('@')
            else:
                new_row.append(large_grid.rows[row][col])
        new_rows.append("".join(new_row))

    return remove_count, LargeGrid(new_rows)


def part1() -> None:
    large_grid = read_input()

    solution = sum([
        1 if large_grid.rows[row][col] == "@" and large_grid.has_fewer_than_four_adjacent_rolls(row, col) else 0
        for row in range(0, len(large_grid.rows))
        for col in range(0, len(large_grid.rows[row]))
    ])

    print(solution)


def part2() -> None:
    large_grid = read_input()

    total_removed = 0
    while True:
        (remove_count, large_grid) = remove_rolls_of_paper(large_grid)
        if remove_count == 0:
            break

        total_removed += remove_count

    print(total_removed)


if __name__ == "__main__":
    part1()
    part2()
