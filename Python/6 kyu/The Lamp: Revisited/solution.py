# [6 kyu] The Lamp: Revisited
#
# Author:   Hsins
# Date:     2019/12/23


class Lamp(object):
    def __init__(self, color=None, on=False):
        self.color = color
        self.on = on

    def toggle_switch(self):
        # self.on ^= 1
        self.on = not self.on

    def state(self):
        return "The lamp is {}.".format("on" if self.on else "off")
