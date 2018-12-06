#!/usr/bin/env python

import advent

def main():
    input = advent.getInput(5)
    part_1(input)
    part_2(input)

def part_1(s):
    tokens = get_tokens(s)

    while True:
    	p = process_tokens(tokens)
    	if p == tokens:
    		break
    	else:
    		tokens = p

    print(len(tokens))

def part_2(s):
    tokens = get_tokens(s)

    unique_types = set([t["type"] for t in tokens])

    best_n = len(tokens)

    for type in unique_types:
        modified_polymer = [t for t in tokens if t["type"] != type]
        reacted = process_tokens(modified_polymer)

        reacted_n = len(reacted)

        if reacted_n < best_n:
            best_n = reacted_n

    print(best_n)



def get_tokens(string):
    return [{"char": c, "type": get_type(c), "pol": get_polarization(c)} for c in string]

def process_tokens(tokens):
    keep = [True for t in tokens]

    cursor = [0, 1]
    n = len(tokens)

    while cursor[1] < n:
        token_1 = tokens[cursor[0]]
        token_2 = tokens[cursor[1]]

        if keep[cursor[0]] != keep[cursor[1]]:
            if cursor[0] == 0:
                cursor[0] = cursor[1]
                cursor[1] += 1
            else:
                while keep[cursor[0]] != keep[cursor[1]] and cursor[0] > 0:
                    cursor[0] -= 1
        elif annihilate(token_1, token_2):
            keep[cursor[0]] = False
            keep[cursor[1]] = False
            cursor[0] == max(0, cursor[0] - 1)
            cursor[1] += 1
        else:
            cursor[1] += 1
            cursor[0] = cursor[1] - 1

    return [tokens[i] for i in range(len(tokens)) if keep[i]]




def annihilate(token_1, token_2):
    return (token_1["type"] == token_2["type"]) and (token_1["pol"] != token_2["pol"])

def get_type(c):
	return c.upper()

def get_polarization(c):
	return 1 if (c == c.upper()) else 0

if __name__ == "__main__":
    main()
