# setup.py

from setuptools import setup, find_packages

setup(
    name="hello-world-package",
    version="0.1",
    description="A simple greeting package",
    author="Jean Franco",
    author_email="jfranco1989@gmail.com",
    license="MIT",
    long_description_content_type="text/markdown",
    url="https://github.com/jfranco1989/hello-world-package.git",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
