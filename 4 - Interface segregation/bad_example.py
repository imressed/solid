# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Данный интефейс плох тем, что он включает слишком много методов.
А что, если наш класс товаров не может иметь скидок или промокодов,
либо для него нет смысла устанавливать материал из которого сделан (например, для книг).
Таким образом, чтобы не реализовывать в каждом классе неиспользуемые в нём методы,
лучше разбить интерфейс на несколько мелких и
каждым конкретным классом реализовывать нужные интерфейсы."""


class IItem(object):

    def apply_discount(self, discount):
        pass
    def apply_promocode(self, promo):
        pass

    def set_color(self, color):
        pass
    def set_size(self, size):
        pass

    def set_condition(self, condition):
        pass
    def set_price(self, price):
        pass

