import setuptools

import pkg_resources
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    install_requires = [str(req) for req in pkg_resources.parse_requirements(f)]

setuptools.setup(
    name="blindtex",
    version="0.0.1",
    author="BlindTeX Team",
    author_email="blindtexunal@gmail.com",
    description="A package for converter LaTeX equations to natural language and more!.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blindtex/blindtex/",
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires=install_requires,
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
    #entry_points={
    #      'console_scripts': [
    #          'blindtex = blindtex.blindtex:main'
    #      ]
    #  }
)
