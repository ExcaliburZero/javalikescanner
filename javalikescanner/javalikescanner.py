"""A module containg the JavaLikeScanner class."""

class JavaLikeScanner:
	"""A class which allows a given string to be scanned through and broken
	up into various tokens."""

	def __init__(self, contents):
		"""Create the scanner and initalize its contents."""
		self.contents = contents

	def __get_token(self):
		"""Find and return the next token and its pre-delimiters if it has any.

		:returns: The next token and its pre-delimiters as a dictionary.
		"""
		token_info = {'token': "", 'pre-delimiter': ""}

		# If the scanner has contents, then look for the next token
		if len(self.contents) > 0:
			# Check over each character in the scanner until a token is found, or the end of the scanner is
			# reached
			for character in self.contents:
				if character != " " and character != "\n" and character != "\t":
					# If the character is not a delimiter, then add it to the token
					token_info['token'] = token_info['token'] + character
				else:
					if len(token_info['token']) == 0:
						# If a token character hasn't been found yet, then the delimiter must be a pre-delimiter
						token_info['pre-delimiter'] = token_info['pre-delimiter'] + character
					else:
						# Since the next delimiter has been reached after the token, then break to return the token
						break
		# If a token was found, then return the token and pre-delimiters
		if token_info['token'] != "":
			return token_info
		else:
			# Since no token was found, return None
			return None

	def has_next(self):
		"""Return whether or not there is a valid next token in the
		scanner or not.

		:returns: Whether or not there is a next token in the scanner
		as a boolean.
		"""
		token = self.__get_token()
		if token is not None:
			return True
		else:
			return False

	def next(self):
		"""Return the next token in the scanner and remove that token
		from the scanner.

		:returns: The next token in the scanner as a string.
		"""
		if self.has_next():
			# Since there is a next token, remove the token and its pre-delimiters from the scanner, and
			# return the token
			token = self.__get_token()
			size = len(token['pre-delimiter']) + len(token['token'])
			self.contents = self.contents[size:]
			return token['token']
		else:
			# Since there is no next token in the scanner, return None
			return None

	def has_next_line(self):
		"""Return whether or not there is a next line in the scanner.

		:returns: Whether or not there is a next line in the scanner as
		a boolean.
		"""
		if self.contents != "":
			return True
		else:
			return False

	def next_line(self):
		"""Return the next line in the scanner and remove that line from
		the scanner.

		:returns: The next line in the scanner as a string.
		"""
		if self.has_next_line():
			line = ""
			has_delimiter = False
			for character in self.contents:
				if character != "\n":
					line = line + character
				else:
					has_delimiter = True
					break
			size = len(line)
			# Account for the delimiter
			if has_delimiter:
				size = size + 1
			self.contents = self.contents[size:]
			return line
		else:
			return None

	def has_next_int(self):
		"""Return whether the next token in the scanner is an integer
		or not.

		:returns: Whether or not the next token in the scanner is an
		integer as a boolean.
		"""
		token = self.__get_token()

		# Handle the possiblity of an empty token
		if token == None:
			return False

		# Attempt to convert the token into an integer in order to tell if it is an integer or not
		try:
			int(token['token'])
			return True
		except ValueError:
			return False

	def next_int(self):
		"""Return the next integer in the scanner and remove that
		integer from the scanner.

		:returns: The next integer in the scanner as an integer.
		"""
		if self.has_next_int():
			token = self.__get_token()
			token_integer = int(token['token'])

			# Remove the token and its pre-delimiters from the scanner and return it
			size = len(token['pre-delimiter']) + len(token['token'])
			self.contents = self.contents[size:]
			return token_integer
		else:
			return None
