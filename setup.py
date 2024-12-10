from setuptools import setup, find_packages

setup(
    name="ascii_dice",
    version="1.0.0",
    author="Simon Benzer",
    author_email="SimonHBenzer@gmail.com",
    description="Python library that simulates dice rolling and Dungeons & Dragons (D&D) calculations with ASCII images",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shbenzer/ascii_dice",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)