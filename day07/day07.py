import dataclasses
import pathlib


@dataclasses.dataclass
class Diagram:
    rows: list[str]

    def __str__(self) -> str:
        return '\n'.join(self.rows)


@dataclasses.dataclass
class TachyonBeamTracer:
    beams: set[tuple[int, int]]


def read_input() -> list[str]:
    return (pathlib.Path(__file__).parent / "input.txt").read_text().splitlines()


def show(diagram: Diagram, tracer: TachyonBeamTracer) -> None:
    for r, line in enumerate(diagram.rows):
        for c, cell in enumerate(list(line)):
            if (r, c) in tracer.beams:
                print('|', end='')
            else:
                print(cell, end='')
        print()


def part1() -> None:
    diagram = Diagram(read_input())
    tracer = TachyonBeamTracer(set())

    tracer.beams.add((0, diagram.rows[0].find('S')))

    split_count = 0

    for r, line in enumerate(diagram.rows):
        for c, cell in enumerate(list(line)):
            if cell == '.':
                if (r - 1, c) in tracer.beams:
                    tracer.beams.add((r, c))
            elif cell == '^':
                if (r - 1, c) in tracer.beams:
                    split_count += 1
                    tracer.beams.add((r, c - 1))
                    tracer.beams.add((r, c + 1))

    print(split_count)


def part2() -> None:
    way_to_get_to: dict[tuple[int, int], int] = dict()
    way_to_get_to[(0, 0)] = 5

    diagram = Diagram(read_input())

    solution = sum([
        timeline_count(diagram, len(diagram.rows) - 1, c)
        for c in range(0, len(diagram.rows[0]))
    ])

    print(solution)


way_to_get_to: dict[tuple[int, int], int] = {}


def timeline_count(diagram: Diagram, r: int, c: int) -> int:
    if r == 0:
        if c == diagram.rows[0].find('S'):
            return 1
        else:
            return 0

    if c < 0 or c >= len(diagram.rows[0]):
        return 0

    if r % 2 == 1:
        return timeline_count(diagram, r - 1, c)

    if (r, c) in way_to_get_to:
        return way_to_get_to[(r, c)]

    if diagram.rows[r][c] == '.':
        total_ways_to_reach = 0

        if c - 1 >= 0 and diagram.rows[r][c - 1] == '^':
            from_left = timeline_count(diagram, r - 1, c - 1)
            way_to_get_to[(r - 1, c - 1)] = from_left
            total_ways_to_reach += from_left

        if c + 1 < len(diagram.rows[0]) and diagram.rows[r][c + 1] == '^':
            from_right = timeline_count(diagram, r - 1, c + 1)
            way_to_get_to[(r - 1, c + 1)] = from_right
            total_ways_to_reach += from_right

        total_ways_to_reach += timeline_count(diagram, r - 1, c)
        way_to_get_to[(r, c)] = total_ways_to_reach
        return total_ways_to_reach

    return 0


if __name__ == "__main__":
    part1()
    part2()
