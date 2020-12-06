import numpy as np
import re


def part1(data):
    num_valid = 0
    for line in data.split('\n'):
        match = re.match(r'(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)', line)
        if not match:
            continue
        min_entries, max_entries, entry, password = match.groups()
        if password.count(entry) in range(int(min_entries), int(max_entries) + 1):
            num_valid += 1
    return num_valid


def part2(data):
    num_valid = 0
    for line in data.split('\n'):
        match = re.match(r'(\d+)-(\d+) ([a-zA-Z]): ([a-zA-Z]+)', line)
        if not match:
            continue
        loc1, loc2, entry, password = match.groups()
        matches = [i + 1 for i, ch in enumerate(password) if ch == entry]
        if matches and ((int(loc1) in matches) ^ (int(loc2) in matches)):
            num_valid += 1
    return num_valid
