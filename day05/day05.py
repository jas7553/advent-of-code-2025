import dataclasses
import pathlib
import re


@dataclasses.dataclass
class FreshIngredientIdRange:
    start: int
    end: int

    def __str__(self):
        return f"{self.start}–{self.end}"


def read_input() -> tuple[list[FreshIngredientIdRange], list[int]]:
    range_pattern = re.compile(r"^\d+-\d+$")
    single_digit_pattern = re.compile(r"^\d+$")

    fresh_ingredient_id_ranges = []
    ingredient_ids = []

    with open((pathlib.Path(__file__).parent / "input.txt")) as f:
        for line in f:
            line = line.strip()
            if range_pattern.fullmatch(line):
                pieces = line.split("-")
                fresh_ingredient_id_ranges.append(FreshIngredientIdRange(int(pieces[0]), int(pieces[1])))
            elif single_digit_pattern.fullmatch(line):
                ingredient_ids.append(int(line))
            else:
                continue

    return fresh_ingredient_id_ranges, ingredient_ids


def is_fresh(fresh_ids: list[FreshIngredientIdRange], ingredient_id: int) -> bool:
    return any(id_range.end >= ingredient_id >= id_range.start for id_range in fresh_ids)


def part1() -> None:
    fresh_ingredient_id_ranges, ingredient_ids = read_input()

    solution = sum(
        1
        for ingredient_id in ingredient_ids
        if is_fresh(fresh_ingredient_id_ranges, ingredient_id)
    )

    print(solution)


def part2() -> None:
    pass


if __name__ == "__main__":
    part1()
    part2()
