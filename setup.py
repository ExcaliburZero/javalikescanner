"""The script which is used when packaging the library."""
from setuptools import setup

setup( \
      name='javalikescanner',
      version='0.1',
      description='A Python library which includes a class which functions' + \
            'simmilarly to the default Scanner class of Java.',
      long_description=open('README.rst').read(),
      url='https://github.com/ExcaliburZero/javalikescanner',
      author='Christopher Randall Wells',
      author_email='cwellsny@nycap.rr.com',
      license='MIT',
      packages=['javalikescanner'],
      install_requires=[
          'numpy',
      ],
      include_package_data=True,
      package_data={
          '': 'LICENSE'
      },

      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Operating System :: OS Independent',
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ]
     )
