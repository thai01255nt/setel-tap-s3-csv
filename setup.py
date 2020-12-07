#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='setel-tap-s3-csv',
      version='1.2.0',
      description='Singer.io tap for extracting CSV files from S3 - Setel compatible',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Setel',
      url='https://github.com/thai01255nt/setel-tap-s3-csv',
      classifiers=[
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3 :: Only'
      ],
      py_modules=['tap_s3_csv'],
      install_requires=[
          'boto3==1.9.57',
          'singer-encodings==0.0.*',
          'pipelinewise-singer-python==1.*',
          'voluptuous==0.10.5',
          'ujson==1.35.*',
          'messytables==0.15.*',
          'pipelinewise-tap-s3-csv==1.*',
      ],
      extras_require={
          'dev': [
              'ipdb==0.11',
          ],
          'test': [
              'nose==1.3.*',
              'pylint==2.4.*',
          ]
      },
      entry_points='''
          [console_scripts]
          tap-s3-csv=setel_tap_s3_csv:main
      ''',
      packages=['setel_tap_s3_csv'])
