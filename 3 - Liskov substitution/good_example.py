# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Объекты в программе могут быть заменены их наследниками без изменения свойств программы.
 Своими словами я бы это сказал так — при использовании наследника класса результат
 выполнения кода должен быть предсказуем и не изменять свойств метод."""


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


class Square:
    size = 0

    def set_size(self, size):
        self.size = size

    def get_size(self):
        return self.size