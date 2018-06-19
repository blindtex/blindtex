import setuptools

import pkg_resources

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    install_requires = [str(req) for req in pkg_resources.parse_requirements(f)]

setuptools.setup(
    name="latex2ast",
    version="0.0.1",
    author="BlindTeX Team",
    author_email="blindtexunal@gmail.com",
    description="A package for converter LaTeX equations to pseudo AST.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/blindtex/latex2ast/",
    packages=setuptools.find_packages(exclude=['*test*']),
    install_requires=install_requires,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
