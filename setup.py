"""Setup for the sttable package."""

import setuptools

with open('README.rst', encoding='utf-8') as f:
    README = f.read()

setuptools.setup(
    author="aBulgakoff",
    author_email="a.p.bulgakoff@gmail.com",
    name='sttable',
    license="MIT",
    description='Parser of string representation tables',
    version='v0.0.1',
    long_description=README,
    long_description_content_type='text/x-rst',
    url='https://github.com/aBulgakoff/sttable',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
