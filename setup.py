#!/usr/bin/env python
import setuptools


def get_version(filename):
    with open(filename) as in_fh:
        for line in in_fh:
            if line.startswith('__version__'):
                return line.split('=')[1].strip()[1:-1]
    raise ValueError("Cannot extract version from %s" % filename)


setuptools.setup(
    name="casoff-vcf",
    version=get_version("casoff_vcf.py"),
    url="https://github.com/DamLabResources/casoff-vcf",
    author="Will Dampier",
    author_email="judowill@gmail.com",
    description="Wrapper for cas9 off-finder to find matches with SNPs",
    install_requires=[
        'Click',
    ],
    extras_require={'dev': ['pytest',]},
    py_modules=['casoff_vcf'],
    entry_points='''
        [console_scripts]
        casoff-vcf=casoff_vcf:main
    ''',
    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
