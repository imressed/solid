# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Зависимости внутри системы строятся на основе абстракций.
Модули верхнего уровня не зависят от модулей нижнего уровня.
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
Данное определение можно сократить —
зависимости должны строится относительно абстракций, а не деталей."""


class Customer:
    current_order = None

    def buy_items(self, order_processor):
        return order_processor.checkout(self.current_order)


class IOrderProcessor:

    def checkout(self, order):
        pass

class OrderProcessor(IOrderProcessor):

    def checkout(self, order):
        "Do some cool stuff"
        pass