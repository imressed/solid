# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Preconditions can not be strengthened in the subclass
   Postconditions can not be weakened in a subclass
"""

class Rectangle:
    width, height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


class Square(Rectangle):

    def set_width(self, width):
        super(Square, self).set_width(width)
        super(Square, self).set_height(width)

    def set_height(self, height):
        super(Square, self).set_width(height)
        super(Square, self).set_height(height)