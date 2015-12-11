"""A module which defines the eceptions thrown by the JavaLikeScanner class."""

class NoSuchElementException(Exception):
	"""
	An exception which is raised when a token is attempted to be accessed and there is no next token in the scanner.
	"""
	pass

class InputMismatchException(Exception):
	"""
	An exception which is raised when a specific type of token is requested, such as an integer, and the next token in the scanner is not of that type.
	"""
	pass
