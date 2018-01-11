#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="BlindTex",
      description="LaTeX ecuation processing",
      version="0.1",
      author="BlindTex Team",
      author_email="",
      #url="",
      packages = [
      ],
      package_data = {
      },
      scripts=['blindtext/blindTex'],
)
