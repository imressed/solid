# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Много специализированных интерфейсов лучше, чем один универсальный.
Соблюдение этого принципа необходимо для того, чтобы классы-клиенты
использующий/реализующий интерфейс знали только о тех методах, которые они используют,
что ведёт к уменьшению количества неиспользуемого кода."""


class IItem(object):

    def set_condition(self, condition):
        pass

    def set_price(self, price):
        pass


class ICloses(object):

    def set_color(self, color):
        pass

    def set_size(self, size):
        pass


class IDiscountable(object):

    def set_promocode(self, promo):
        pass

    def set_discount(self, discount):
        pass