import dataclasses
import itertools
import math
import pathlib


@dataclasses.dataclass(frozen=True)
class Coordinate:
    x: int
    y: int
    z: int

    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    __repr__ = __str__


def read_input() -> list[str]:
    return (pathlib.Path(__file__).parent / "input.txt").read_text().splitlines()


def compare_distance_between(pair: tuple[Coordinate, Coordinate]) -> float:
    return distance_between(pair[0], pair[1])


def distance_between(q1: Coordinate, q2: Coordinate) -> float:
    return math.sqrt(sum(((q1.x - q2.x) ** 2, (q1.y - q2.y) ** 2, (q1.z - q2.z) ** 2)))


def part1() -> None:
    coordinates = [
        Coordinate(*map(int, line.split(',')))
        for line in read_input()
    ]

    pairs = list(itertools.combinations(coordinates, 2))
    pairs.sort(key=compare_distance_between)

    circuits: list[list[Coordinate]] = [
        [coordinate]
        for coordinate in coordinates
    ]

    for pair in pairs[0:1000]:
        circuit_a = next((circuit for circuit in circuits if pair[0] in circuit))
        circuit_b = next((circuit for circuit in circuits if pair[1] in circuit))

        if circuit_a is not circuit_b:
            circuits.remove(circuit_a)
            circuits.remove(circuit_b)
            circuits.append([*circuit_a, *circuit_b])

    lengths = [len(circuit) for circuit in circuits]
    lengths.sort(reverse=True)
    print(math.prod((length for length in lengths[0:3])))


def part2() -> None:
    coordinates = [
        Coordinate(*map(int, line.split(',')))
        for line in read_input()
    ]

    pairs = list(itertools.combinations(coordinates, 2))
    pairs.sort(key=compare_distance_between)

    circuits: list[list[Coordinate]] = [
        [coordinate]
        for coordinate in coordinates
    ]

    for pair in pairs:
        circuit_a = next((circuit for circuit in circuits if pair[0] in circuit))
        circuit_b = next((circuit for circuit in circuits if pair[1] in circuit))

        if circuit_a is not circuit_b:
            circuits.remove(circuit_a)
            circuits.remove(circuit_b)
            circuits.append([*circuit_a, *circuit_b])

        if len(circuits) == 1:
            print(pair[0].x * pair[1].x)
            break


if __name__ == "__main__":
    part1()
    part2()
