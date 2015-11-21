"""A module containg the JavaLikeScanner class."""

class JavaLikeScanner:
	"""A class which allows a given string to be scanend through and broken
	up into various tokens."""

	def __init__(self, contents):
		"""Create the scanner and initalize its contents."""
		self.contents = contents
		self.last_delimiter = ""

	def next(self):
		"""Return the next token in the scanner and remove that token
		from the scanner."""
		next_token = ""
		self.last_delimiter = ""
		if len(self.contents) > 0:
			for character in self.contents:
				self.contents = self.contents[1:]
				if character != " " and character != "\n" and character != "\t":
					next_token = next_token + character

					# Remove any proceeding delimiters
					self.last_delimiter = ""
				else:
					# Record the delimeters used, so that they can be readded later if an operation
					# does not succede
					self.last_delimiter = self.last_delimiter + character

					# Check to make sure that a token has been found
					if next_token != "":
						break
			# Readd ending delimiters if they were found
			self.contents = self.last_delimiter + self.contents

		if next_token != "":
			self.last_delimiter = ""
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

	def next_int(self):
		"""Return the next integer in the scanner and remove that
		integer from the scanner."""
		token = self.next()

		# Handle the possiblity of an empty token
		if token == None:
			token = ""

		try:
			token_integer = int(token)
			return token_integer
		except ValueError:
			# Since the token was not an integer, readd the token and the delimiter back into the scanner
			if token != "":
				self.contents = token + self.last_delimiter + self.contents
			return None
