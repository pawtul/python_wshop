import unittest

from funkcje import mnozenie, dzielenie


class SuperTest(unittest.TestCase):
	def test_mnozenie(self):
		self.assertEquals(mnozenie(2), 4)
		self.assertEquals(mnozenie(3), 6)

	def test_dzielenie(self):
		self.assertEquals(dzielenie(4), 1)	# to sie wywali bo 2 != 1


if __name__ == "__main__":
	unittest.main()
