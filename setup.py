#!/usr/bin/env python

from distutils.core import setup
from ArtisinalInts import __version__ as version

setup(name='ArtisinalInts',
      version=version,
      description='Interface to hand-crafted integers from Brooklyn and San Francisco.',
      author='Michal Migurski',
      author_email='mike@teczno.com',
      url='https://github.com/migurski/ArtisinalInts',
      packages=['ArtisinalInts'],
    # download_url='https://github.com/downloads/migurski' % locals(),
      license='BSD')
