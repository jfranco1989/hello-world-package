from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requiremnts.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="Jean Franco",
    author_email="jfranco1989@gmail.com",
    description="Pacote para processar comparações entre imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)