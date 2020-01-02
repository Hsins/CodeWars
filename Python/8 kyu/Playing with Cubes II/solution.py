# [8 kyu] Playing with Cubes II
#
# Author:   Hsins
# Date:     2020/01/02


class Cube(object):
    def __init__(self):
        self._side = 0

    def get_side(self):
        """Return the side of the Cube"""
        return self._side

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = abs(new_side)
