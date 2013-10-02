from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")



class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='xls-neo4j',
    version=find_version('xls-neo4j', '__init__.py'),
    url='http://github.com/shaikatzir/xls-neo4j/',
    license='Apache Software License',
    author='Shai Katzir',
    tests_require=['pytest'],
    install_requires=['argparse>=1.2.1',
                      'wsgiref>=0.1.2'
                      ],
    cmdclass={'test': PyTest},
#    author_email='jeff@jeffknupp.com',
    description='Export Neo4j DB data into a spreadsheet',
    packages=['xls-neo4j'],
    include_package_data=True,
    platforms='any',
#    test_suite='sandman.test.test_sandman',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
#    scripts = ['go_foo.py'],
    extras_require={
        'testing': ['pytest'],
      }
)
