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
    fresh_ingredient_id_ranges, _ = read_input()

    fresh_ingredient_id_ranges.sort(key=lambda id_range: id_range.start)

    first_id_range = fresh_ingredient_id_ranges[0]
    small, big = first_id_range.start, first_id_range.end

    ranges = []
    for id_range in fresh_ingredient_id_ranges[1:]:
        if id_range.start > big:
            ranges.append((small, big))
            small, big = id_range.start, id_range.end
        elif id_range.start >= small and id_range.end > big:
            small, big = small, id_range.end

    ranges.append((small, big))

    solution = sum([
        id_range[1] - id_range[0] + 1
        for id_range in ranges
    ])

    print(solution)


if __name__ == "__main__":
    part1()
    part2()
