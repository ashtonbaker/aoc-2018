#!/usr/bin/env python

import advent

def main():
    input = advent.getInput(5)
    part_1(input)

def part_1(s):
    tokens = [{"char": c, "type": get_type(c), "pol": get_polarization(c)} for c in s]

    while True:
    	p = process_tokens(tokens)
    	if p == tokens:
    		break
    	else:
    		tokens = p

    print(len(tokens))

def process_tokens(tokens):
	result = []

	n = len(tokens)

	skip = False
	for i in range(n):
		(token_1, token_2) = (tokens[i], tokens[min(i + 1, n - 1)])
		if skip:
			skip = False
		elif (token_1["type"] == token_2["type"]) and (token_1["pol"] != token_2["pol"]):
			skip = True
		else:
			skip = False
			result.append(token_1)

	return result

def get_type(c):
	return c.upper()

def get_polarization(c):
	return 1 if (c == c.upper()) else 0

if __name__ == "__main__":
    main()