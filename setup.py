import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="file-explorer-utils",
    version="1.1.0",
    description="Useful functions for file explorer",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Tlalocan/file-explorer-utils",
    author="Tlalocan",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["file_explorer_utils"],
    include_package_data=True,
)
