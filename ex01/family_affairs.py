#!/usr/bin/env python3

def find_the_redheads(family_dict):
    # Use filter to get only the items where hair color is "red"
    # Then, extract just the keys (first names) into a list
    redheads = list(filter(lambda name: family_dict[name] == "red", family_dict.keys()))
    return redheads

# Provided test case
dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))