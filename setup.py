import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="cowin-vaccine-api",
    version="0.0.2",
    description="API wrapper for Cowin Api",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/its-k/cowin-api",
    author="Kishore",
    author_email="kishore4110@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["cowin"],
    include_package_data=True,
    install_requires=['requests','fake_useragent','datetime'],
    entry_points={
        "console_scripts": [
            "cowin=cowin.__main__:main",
        ]
    },
)
