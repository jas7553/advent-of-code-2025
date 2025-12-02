import dataclasses
import pathlib
from enum import Enum
from typing import Iterable

BASE_DIR = pathlib.Path(__file__).parent

class Direction(str, Enum):
    RIGHT = "R"
    LEFT = "L"

@dataclasses.dataclass(frozen=True)
class Rotation:
    direction: Direction
    clicks: int

    def __str__(self) -> str:
        return f"{self.direction.value}{self.clicks}"

def read_rotations() -> Iterable[Rotation]:
    with open(BASE_DIR / "input.txt", "r") as f:
        for line in f:
            text = line.strip()
            yield Rotation(Direction(text[0]), int(text[1:]))

def part1() -> None:
    pointing_at = 50
    dial_at_zero_count = 0

    for rotation in read_rotations():
        delta = rotation.clicks if rotation.direction == Direction.RIGHT else -rotation.clicks
        pointing_at = (pointing_at + delta) % 100
        if pointing_at == 0:
            dial_at_zero_count += 1

    print(dial_at_zero_count)

def part2() -> None:
    pointing_at = 50
    dial_at_zero_count = 0

    for rotation in read_rotations():
        full_rotations = rotation.clicks // 100
        dial_at_zero_count += full_rotations

        remaining_clicks = rotation.clicks % 100

        delta = remaining_clicks if rotation.direction == Direction.RIGHT else -remaining_clicks
        new_pointing_at = (pointing_at + delta) % 100

        if new_pointing_at == 0:
            dial_at_zero_count += 1
        elif pointing_at != 0:
            if (rotation.direction == Direction.RIGHT and new_pointing_at < pointing_at) or (rotation.direction == Direction.LEFT and new_pointing_at > pointing_at):
                dial_at_zero_count += 1

        pointing_at = new_pointing_at

    print(dial_at_zero_count)

if __name__ == "__main__":
    part1()
    part2()
