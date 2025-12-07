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
    pass


if __name__ == "__main__":
    part1()
    part2()
