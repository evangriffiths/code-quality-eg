import pprint
import json

import os


def  a_weird_function(
    x: list[int]) ->int:
            y = x[0]
            z = x[2]
            a = 1
            return 2    * (y + z    )

pprint.pprint(a_weird_function([1, 2, 3]))
os.environ["key"] = 'value'
