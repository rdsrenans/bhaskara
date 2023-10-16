from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="bhaskara",
    version="0.0.1",
    author="Renan de Souza",
    author_email="example@mail.com",
    description="Lib para calculo de Bhaskara com plot",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rdsrenans/bhaskara",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)