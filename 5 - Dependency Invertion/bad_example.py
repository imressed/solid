# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""Всё кажется вполне логичным и закономерным. Но есть одна проблема —
класс Customer зависит от класса OrderProcessor
(мало того, не выполняется и принцип открытости/закрытости).
Для того, чтобы избавится от зависимости от конкретного класса,
надо сделать так чтобы Customer зависел от абстракции,
т.е. от интерфейса IOrderProcessor."""


class Customer:
    current_order = None

    def buy_items(self):
        processor = OrderProcessor()
        return processor.checkout(self.current_order)


class OrderProcessor:

    def checkout(self, order):
        pass