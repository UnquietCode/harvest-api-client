#!/usr/bin/env python

from distutils.core import setup, find_packages

setup(
    name='harvest_api_client',
    version='1.0.1',
    description='A library for working with Harvest API (getharvest.com)',
    license='MIT',
    author='Alex Maslakov',
    author_email='me@gildedhonour.com, gilded.honour@gmail.com',
    url='https://www.github.com/harvest-api-client',
    packages=['harvest_api_client'],
    package_data={'': ['LICENSE.txt', 'MANIFEST', 'MANIFEST.IN', 'README.md']}
    include_package_data=True,
    long_description=open('README.md').read(),
    keywords = ['harvest-api', 'api', 'harvest-com', 'getharvest.com'], 
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],  
)