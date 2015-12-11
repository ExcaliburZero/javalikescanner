"""Various tests of the JavaLikeScanner class."""
import unittest

from javalikescanner import JavaLikeScanner
from javalikescanner import NoSuchElementException
from javalikescanner import InputMismatchException

class TestJavaLikeScanner(unittest.TestCase):
	"""A class which defines the various methods used to test the JavaLikeScanner class."""
	def test_next(self):
		"""A test of the next method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("one two three\nfour\tfive six\t")
		self.assertEqual(scanner.next(), "one")
		self.assertEqual(scanner.next(), "two")
		self.assertEqual(scanner.next(), "three")
		self.assertEqual(scanner.next(), "four")
		self.assertEqual(scanner.next(), "five")
		self.assertEqual(scanner.next(), "six")
		error = False
		try:
			scanner.next()
		except NoSuchElementException as exception:
			error = True
		self.assertEqual(error, True)

		scanner = JavaLikeScanner("seven  eight\t\tnine\n\t ten\n\t \t")
		self.assertEqual(scanner.next(), "seven")
		self.assertEqual(scanner.next(), "eight")
		self.assertEqual(scanner.next(), "nine")
		self.assertEqual(scanner.next(), "ten")
		error = False
		try:
			scanner.next()
		except NoSuchElementException as exception:
			error = True
		self.assertEqual(error, True)
		self.assertEqual(scanner.contents, "\n\t \t")

		scanner = JavaLikeScanner("")
		error = False
		try:
			scanner.next()
		except NoSuchElementException as exception:
			error = True
		self.assertEqual(error, True)

	def test_next_line(self):
		"""A test of the next_line method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("one two three\nfour\tfive six")
		self.assertEqual(scanner.next_line(), "one two three")
		self.assertEqual(scanner.next_line(), "four\tfive six")
		error = False
		try:
			scanner.next_line()
		except NoSuchElementException as exception:
			error = True
		self.assertEqual(error, True)
		self.assertEqual(scanner.contents, "")

		scanner = JavaLikeScanner("")
		error = False
		try:
			scanner.next_line()
		except NoSuchElementException as exception:
			error = True
		self.assertEqual(error, True)

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
		for x in range(2):
			error = False
			try:
				scanner.next_int()
			except InputMismatchException as exception:
				error = True
			self.assertEqual(error, True)

		scanner = JavaLikeScanner("1 \t2 1.5\t5")
		self.assertEqual(scanner.next_int(), 1)
		self.assertEqual(scanner.next_int(), 2)
		for x in range(2):
			error = False
			try:
				scanner.next_int()
			except InputMismatchException as exception:
				error = True
			self.assertEqual(error, True)
		self.assertEqual(scanner.contents, " 1.5\t5")

		scanner = JavaLikeScanner("1\t \t")
		self.assertEqual(scanner.next_int(), 1)
		for x in range(2):
			error = False
			try:
				scanner.next_int()
			except NoSuchElementException as exception:
				error = True
			self.assertEqual(error, True)
		self.assertEqual(scanner.contents, "\t \t")

		scanner = JavaLikeScanner("")
		error = False
		try:
			scanner.next_int()
		except NoSuchElementException as exception:
			error = True
		self.assertEqual(error, True)

	def test_has_next(self):
		"""A test of the has_next method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("test")
		self.assertEqual(scanner.has_next(), True)
		self.assertEqual(scanner.contents, "test")

		scanner = JavaLikeScanner("\t\ttest2")
		self.assertEqual(scanner.has_next(), True)
		self.assertEqual(scanner.contents, "\t\ttest2")

		scanner = JavaLikeScanner("\t\t")
		self.assertEqual(scanner.has_next(), False)

	def test_has_next_line(self):
		"""A test of the has_next_line method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("one two three")
		self.assertEqual(scanner.has_next_line(), True)

		scanner = JavaLikeScanner("")
		self.assertEqual(scanner.has_next_line(), False)

		scanner = JavaLikeScanner("one two three\n")
		self.assertEqual(scanner.has_next_line(), True)

	def test_has_next_int(self):
		"""A test of the has_next_int method of the JavaLikeScanner class."""
		scanner = JavaLikeScanner("1234")
		self.assertEqual(scanner.has_next_int(), True)
		self.assertEqual(scanner.contents, "1234")

		scanner = JavaLikeScanner("1.2")
		self.assertEqual(scanner.has_next_int(), False)
		self.assertEqual(scanner.contents, "1.2")

		scanner = JavaLikeScanner("\t\t1234")
		self.assertEqual(scanner.has_next_int(), True)
		self.assertEqual(scanner.contents, "\t\t1234")

		scanner = JavaLikeScanner("\t\t")
		self.assertEqual(scanner.has_next_int(), False)
		self.assertEqual(scanner.contents, "\t\t")

		scanner = JavaLikeScanner("")
		self.assertEqual(scanner.has_next_int(), False)
		self.assertEqual(scanner.contents, "")

if __name__ == '__main__':
	unittest.main()
