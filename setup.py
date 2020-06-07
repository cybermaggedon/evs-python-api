import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="evs-python-api",
    version="0.1",
    author="cybermaggedon",
    author_email="cybermaggedon@gmail.com",
    description="Cyberprobe eventstream API for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cybermaggedon/evs-python-api",
    packages=setuptools.find_packages(),
    install_requires=[
        'prometheus_client', 'pulsar-client'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
