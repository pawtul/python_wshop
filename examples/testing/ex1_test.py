# -*- encoding: utf-8 -*-
import unittest


class PrzykladowyTestCase(unittest.TestCase):  # definiujemy test case - dziedziczy po unittest.TestCase
    @classmethod
    def setUpClass(cls):  # metoda wykonywana przed każdym testem
        pass

    def setUp(self):  # metoda wykonywana przed każdym testem
        pass

    def test_add(self):  # metody-testy zaczynają się ok test_
        self.assertEqual(2+2, 4, ':(')  # testuje, czy pierwszy argument jest równy drugiemu
                                        # jeżeli nie, na ekran zostanie wypisany trzeci argument

    def tearDown(self):  # metoda wywoływana po każdym tescie
        pass

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()  # odpalenie testu z linii komend

