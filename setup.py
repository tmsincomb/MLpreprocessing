#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = [
    "Click>=7.0",
    "pandas",
    "biopython",
    "pysam",
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Troy Sincomb",
    author_email="troysincomb@gmail.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    description="Read bioinformatics sequence formats into a Pandas DataFrame",
    entry_points={
        "console_scripts": [
            "seqpandas=seqpandas.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="seqpandas",
    name="seqpandas",
    packages=find_packages(include=["seqpandas", "seqpandas.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/tmsincomb/seqpandas",
    version="0.0.2",
    zip_safe=False,
)
