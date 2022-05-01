# fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

# print(sorted(fruits, key=lambda fruit: fruit[::-1]))

# print([n for n in sorted()])


# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     print(it)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer

#     for element in it:
#         value = function(value, element)
#     return value
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function([value, element])
#     return value


# print(reduce(sum, [1, 2, 3, 4]))

# import html
# from msilib import sequence


# def make_element(name, value, **attrs):
#     keyvals = [f' {key}="{value}"' for key, value in attrs.items()]
#     attr_str = ''.join(keyvals)
#     element = f'<{name}{attr_str}>{html.escape(value)}</{name}>'
#     return element


# print(make_element('item', 'Albatross', size="large", quantity=6))


# def mininum(*values, clip=None):
#     m = min(values)
#     if clip is not None:
#         m = clip if clip > m else m
#     return m


# def add(x: int, y: int) -> int:
#     return x + y


# print(add.__annotations__)


# class Spam:
#     def bar(self, x: int, y: int):
#         print('Bar 1:', x, y)

#     def bar(self, s: str, n: int = 0):
#         print('Bar 2:', s, n)


# s = Spam()
# s.bar(2, 3)
# s.bar('hello')

# # _no_value = object()

# # def spam(a, b=_no_value):
# #     if b is _no_value:

# names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']
# for name in names:
#     print(name.split()[-1].lower())


# def output_result(result, log=None):
#     if log is not None:
#         log.debug(f'Got: {result}')

# def add(x, y):
#     return x + y

# if __name__ == '__main__':
#     import logging
#     from multiprocessing import Pool
#     from functools import partial

#     logging.basicConfig(level=logging.DEBUG)
#     log = logging.getLogger('test')

#     p = Pool()
#     p.apply_async(add, (3,4), callback=partial(output_result, log=log))
#     p.close()
#     p.jdoin()

from collections import namedtuple
from abc import ABC, abstractmethod
from cgi import print_exception


def apply_async(func: object, args, *, callback: any):
    result = func(*args)
    callback(result)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print(f'[{sequence}] Got: {result}')
    return handler


def add(x, y):
    return x + y


handler = make_handler()
apply_async(add, (2, 3), callback=handler)
print(apply_async.__annotations__)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))
    return handler


handler = make_handler()
handler(7)
handler(8)


Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = print_exception

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = Customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0

        else:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        return f"Order total {self.total()} due: {self.due()}"


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total * .1
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


print([globals()[name] for name in globals() if name.endswith('Promo')])
