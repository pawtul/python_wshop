# -*- encoding: utf-8 -*-

# sprawdzanie czy testowany kod wyrzuca wyjątek
import unittest


def explosion(a, b):
    return a + b


class ExpolsionTestCase(unittest.TestCase):
    def test_addition(self):
        self.assertEquals(explosion(2, 2), 4)

    def test_explosion_explodes(self):
        self.assertRaises(TypeError, explosion, 'Asdf', 4)

        # alternatywnie
        with self.assertRaises(TypeError):
            explosion('Asdf', 4)
