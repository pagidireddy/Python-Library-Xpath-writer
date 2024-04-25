# XPath Generator

XPath Generator is a Python utility for generating XPath expressions for HTML elements on a webpage.

## Installation

You can install XPath Generator via pip:

```
pip install xpath-writer
```

## Usage

```python
import xpath-writer as xw

# Initialize XPathGenerator with the URL of the webpage
generator = xw.Xpath('https://example.com')

# Fetch the webpage content
generator.fetch_page()

# Generate XPath expressions for specific HTML elements
xpaths = generator.xpath_by_tag(tag_name='a')

# Write XPath expressions to an Excel file
write_to_excel(xpaths, 'xpath_output.xlsx')
