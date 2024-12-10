import json # An unused import

import os

import pprint

def add_two_things_together(
        x: int, y: int) -> int:
    z = 1 # An unused variable
    return x +    y

if __name__ == "__main__":
    pprint.pprint(add_two_things_together(1, 2))
    os.environ["key"] = "value"