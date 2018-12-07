#!/usr/bin/env python

import advent
import re

def main():
    input = parse_input(advent.getInput(4))
    part_1(input)
    part_2(input)

def parse_input(string):
	return string.split("\n")

def part_1(lines):
	guards = get_guard_schedules(lines)

	most_sleepy = sorted([(key, sum(value)) for key, value in guards.items()], key=lambda x: x[1], reverse=True)[0][0]

	sleep_schedule = guards[most_sleepy]

	max_minute = sleep_schedule.index(max(sleep_schedule))

	print(most_sleepy * max_minute)

def part_2(lines):
	guards = get_guard_schedules(lines)

	max_guard = 0
	max_minute = 0
	max_sleep = 0

	for k in guards.keys():
		sleep = max(guards[k])
		minute = guards[k].index(sleep)

		if sleep > max_sleep:
			max_sleep = sleep
			max_minute = minute
			max_guard = k

	print(max_guard * max_minute)


def get_guard_schedules(lines):
	lines.sort(key=get_timestamp)

	guards = {}

	current_guard = 0

	for l in lines:
		if "begins shift" in l:
			current_guard = get_guard(l)
			if current_guard not in guards:
				guards[current_guard] = [0] * 60

		elif "falls asleep" in l:
			fell_asleep = get_minute(l)

		elif "wakes up" in l:
			woke_up = get_minute(l)
			cursor = fell_asleep

			while cursor < woke_up:
				guards[current_guard][cursor] += 1
				cursor += 1

	return guards

def get_timestamp(line):
	return int(line[1:5] + line[6:8] + line[9:11] + line[12:14] + line[15:17])

def get_guard(line):
	return int(line.split(" ")[3][1:])

def get_minute(line):
	return int(line[15:17])

if __name__ == "__main__":
    main()