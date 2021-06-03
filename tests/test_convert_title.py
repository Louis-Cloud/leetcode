from convert.convert_title import get_id
import pytest

# Dictionary of titles and expected ids
titles = {
    "Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts":"maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts",
    "Max Area of Island":"max-area-of-island",
    "Interleaving String":"interleaving-string",
}

# Tests to make sure function is converting Leetcode titles to ids correctly
def test_conversion():
    for title, id in titles.items():
        assert id == get_id(title)