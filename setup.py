"""The script which is used when packaging the library."""
from setuptools import setup

setup( \
      name='javalikescanner',
      version='0.1',
      description='A Python library which includes a class which functions' + \
            'simmilarly to the default Scanner class of Java.',
      url='https://github.com/ExcaliburZero/javalikescanner',
      author='Christopher Randall Wells',
      author_email='cwellsny@nycap.rr.com',
      license='MIT',
      packages=['javalikescanner'],
      install_requires=[
          'numpy',
      ]
     )
