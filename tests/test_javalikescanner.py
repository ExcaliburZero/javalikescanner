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

if __name__ == '__main__':
	unittest.main()
