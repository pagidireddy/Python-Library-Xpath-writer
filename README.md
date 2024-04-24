# XPath Generator

XPath Generator is a Python utility for generating XPath expressions for HTML elements on a webpage.

## Installation

You can install XPath Generator via pip:

```
pip install xpath-writer
```

## Usage

```python
from xpath_generator import XPathGenerator, write_to_excel

# Initialize XPathGenerator with the URL of the webpage
generator = XPathGenerator('https://example.com')

# Fetch the webpage content
generator.fetch_page()

# Generate XPath expressions for specific HTML elements
xpaths = generator.generate_xpath(tag_name='a')

# Write XPath expressions to an Excel file
write_to_excel(xpaths, 'xpath_output.xlsx')
