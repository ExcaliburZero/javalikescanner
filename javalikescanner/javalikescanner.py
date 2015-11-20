"""A module containg the JavaLikeScanner class."""

class JavaLikeScanner:
	"""A class which allows a given string to be scanend through and broken
	up into various tokens."""

	def __init__(self, contents):
		"""Create the scanner and initalize its contents."""
		self.contents = contents

	def print_contents(self):
		"""Print out the contents of the scanner."""
		print(self.contents)

	def next(self):
		"""Return the next token in the scanner and remove that token
		from the scanner."""
		next_token = ""
		if len(self.contents) > 0:
			for character in self.contents:
				self.contents = self.contents[1:]
				if character != " " and character != "\n" and character != "\t":
					next_token = next_token + character
				else:
					break
		if next_token != "":
			return next_token
		else:
			return None

	def next_line(self):
		"""Return the next line in the scanner and remove that line from
		the scanner."""
		line = ""
		if len(self.contents) > 0:
			for character in self.contents:
				self.contents = self.contents[1:]
				if character != "\n":
					line = line + character
				else:
					break
		if line != "":
			return line
		else:
			return None
