from setuptools import find_packages, setup

VERSION = "1.0"
DESCRIPTION = "Package for Projects"
LONG_DESCRIPTION = "Package for Leetcode and Trading exercises"

# Setting up
setup(
    name="utils",
    version=VERSION,
    author="Abhishek De",
    author_email="abhishekde95@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=["python", "utils"],
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
    ],
)
