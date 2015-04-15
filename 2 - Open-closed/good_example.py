# -*- coding: utf-8 -*-
__author__ = 'imressed'
"""software entities should be open for extension but closed for modification"""


class OrderRepository:
    source = None

    def setSource(self, source):
        self.source = source

    def load(self, orderid):
        return self.source.load(orderid)

    def save(self):
        pass

    def update(self):
        pass


class OrderSource:
    """Interface for Source"""
    def load(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class MySqlOrderSource(OrderSource):
    """MySql implementation for all methods from OrderSource"""
    def load(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class ApiOrderSource(OrderSource):
    """Api implementation for all methods from OrderSource"""
    def load(self):
        pass

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass