"""Various tests of the JavaLikeScanner class."""
import unittest

from javalikescanner import JavaLikeScanner

class TestJavaLikeScanner(unittest.TestCase):
	"""A class which defines the various methods used to test the JavaLikeScanner class."""
	def test_next(self):
		"""A test of the next method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("one two three\nfour\tfive six")
		self.assertEqual(scanner.next(), "one")
		self.assertEqual(scanner.next(), "two")
		self.assertEqual(scanner.next(), "three")
		self.assertEqual(scanner.next(), "four")
		self.assertEqual(scanner.next(), "five")
		self.assertEqual(scanner.next(), "six")

	def test_next_line(self):
		"""A test of the next_line method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("one two three\nfour\tfive six")
		self.assertEqual(scanner.next_line(), "one two three")
		self.assertEqual(scanner.next_line(), "four\tfive six")

	def test_next_int(self):
		"""A test of the next_int method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("0 1 23 456\n7\t8 9 test 10")
		self.assertEqual(scanner.next_int(), 0)
		self.assertEqual(scanner.next_int(), 1)
		self.assertEqual(scanner.next_int(), 23)
		self.assertEqual(scanner.next_int(), 456)
		self.assertEqual(scanner.next_int(), 7)
		self.assertEqual(scanner.next_int(), 8)
		self.assertEqual(scanner.next_int(), 9)
		self.assertEqual(scanner.next_int(), None)
		self.assertEqual(scanner.next_int(), None)

		scanner = JavaLikeScanner("1 1.5\t5")
		self.assertEqual(scanner.next_int(), 1)
		self.assertEqual(scanner.next_int(), None)
		self.assertEqual(scanner.next_int(), None)
		self.assertEqual(scanner.next_line(), "1.5\t5")

if __name__ == '__main__':
	unittest.main()
