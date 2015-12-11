"""The init file for the javalikescanner package."""
from .javalikescanner import JavaLikeScanner
from .exceptions import NoSuchElementException
from .exceptions import InputMismatchException

__author__ = 'Christopher Randall Wells'
__copyright__ = 'Copyright 2015 Christopher Randall Wells'
__license__ = 'MIT'
__title__ = 'javalikescanner'
__version__ = '0.1'

__all__ = (
    'JavaLikeScanner',
    'NoSuchElementException',
    'InputMismatchException',
)
