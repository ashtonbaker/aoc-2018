#!/usr/bin/env python

import advent

def main():
    input = parse_input(advent.getInput(3))
    part_1(input)
    part_2(input)

def part_1(lines):
    all_claims = [[0 for x in range(1000)] for y in range(1000)]

    for l in lines:

        parsed = l.split(" ")

        (x1, y1) = map(int, parsed[2][:-1].split(','))
        (dx, dy) = map(int, parsed[3].split('x'))
        (x2, y2) = (x1 + dx - 1, y1 + dy - 1)

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                all_claims[y][x] += 1

    result = 0

    for x in range(1000):
        for y in range(1000):
            result += 1 if all_claims[x][y] > 1 else 0

    print(result)


def part_2(lines):
    non_overlapping_claims = set()

    all_claims = [[0 for x in range(1000)] for y in range(1000)]

    for l in lines:

        parsed = l.split(" ")

        claim_number = int(parsed[0][1::])
        (x1, y1) = map(int, parsed[2][:-1].split(','))
        (dx, dy) = map(int, parsed[3].split('x'))
        (x2, y2) = (x1 + dx - 1, y1 + dy - 1)

        non_overlapping_claims.add(claim_number)

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                if all_claims[x][y] == 0:
                    all_claims[x][y] = claim_number
                else:
                    overlapped_claim = all_claims[x][y]
                    if claim_number in non_overlapping_claims:
                        non_overlapping_claims.remove(claim_number)
                    if overlapped_claim in non_overlapping_claims:
                        non_overlapping_claims.remove(overlapped_claim)

    (result,) = non_overlapping_claims

    print(result)

def parse_input(s):
    return s.split("\n")

def line_to_claim(s):
    parsed = s.split(" ")

    (x1, y1) = map(int, parsed[2][:-1].split(','))
    (dx, dy) = map(int, parsed[3].split('x'))
    (x2, y2) = (x1 + dx - 1, y1 + dy - 1)

    claim = [[0] * (x2 + 1)] * (y2 + 1)

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            claim[y][x] = 1
    return claim

if __name__ == "__main__":
    main()