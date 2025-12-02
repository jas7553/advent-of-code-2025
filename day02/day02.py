import dataclasses
import pathlib
from typing import Iterable

BASE_DIR = pathlib.Path(__file__).parent

@dataclasses.dataclass(frozen=True)
class Range:
    start: int
    end: int

    def __str__(self) -> str:
        return f"{self.start}-{self.end}"

def read_input() -> Iterable[Range]:
    with open(BASE_DIR / "input.txt", "r") as f:
        for line in f.readline().split(","):
            pieces = line.strip().split("-")
            yield Range(int(pieces[0]), int(pieces[1]))

def is_invalid_id(product_id: int) -> bool:
    product_id_str = str(product_id)
    midpoint = len(product_id_str) // 2
    return len(product_id_str) % 2 == 0 and product_id_str[:midpoint] == product_id_str[midpoint:]

def is_invalid_id_part2(product_id: int) -> bool:
    product_id_str = str(product_id)
    for i in range(1, len(product_id_str) // 2 + 1):
        if product_id_str[:i] * (len(product_id_str) // i) == product_id_str:
            return True
    return False

def part1() -> None:
    solution = sum(
        product_id
        for range_input in read_input()
        for product_id in range(range_input.start, range_input.end + 1)
        if is_invalid_id(product_id)
    )

    print(solution)

def part2() -> None:
    solution = sum(
        product_id
        for range_input in read_input()
        for product_id in range(range_input.start, range_input.end + 1)
        if is_invalid_id_part2(product_id)
    )

    print(solution)

if __name__ == "__main__":
    part1()
    part2()
