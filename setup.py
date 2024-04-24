from setuptools import setup

setup(
    name="xpath_writer",
    packages=["xpath_writer"],
    version="1.0.1",
    author="Pagidireddy Prasanth Reddy",
    author_email="tradetrontest@gmail.com",
    description="A Python package for writing relative XPath expressions and make XPath Excel file.",
    long_description="The Xpath package provides functionality to extract XPath expressions of elements on a webpage. It utilizes BeautifulSoup for parsing HTML content for interacting with web elements in a browser environment. It utilizes pandas for writing data to Excel file.",
    url="https://github.com/pagidireddy/",
    keywords=['xpath', 'xpath generator', 'xpath writer', 'xpath parser'],
    install_requires=['requests', 'beautifulsoup4', 'pandas', 'openpyxl'],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
