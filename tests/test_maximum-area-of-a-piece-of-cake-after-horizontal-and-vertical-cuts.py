import importlib
solution = importlib.import_module("maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts.solution")

import pytest

inputs = [
    {
        'h' : 5,
        'w' : 4,
        'horizontalCuts' : [1, 2, 4],
        'verticalCuts' : [1, 3],
        'expected': 4
    },
    {
        'h' : 5,
        'w' : 4,
        'horizontalCuts' : [3, 1],
        'verticalCuts' : [1],
        'expected': 6
    },
    {
        'h' : 5,
        'w' : 4,
        'horizontalCuts' : [3],
        'verticalCuts' : [3],
        'expected': 9
    }
]

def test_maxArea():
    for input in inputs:
        temp = solution.Solution()
        actual = temp.maxArea(h=input['h'], w=input['w'], horizontalCuts=input['horizontalCuts'], verticalCuts=input['verticalCuts'])
        expected = input['expected']

        assert actual == expected
