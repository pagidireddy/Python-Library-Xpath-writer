import os
import requests
from bs4 import BeautifulSoup
import pandas as pd


def make_excel(data, filename):
    """
    Write data to Excel file after you fetch the xpath successfully.

    Provide xpath fetched variable as data param.

    Example Usage:

    xpath = xpath_by_tag('span')

    make_excel(xpath, 'xpath.xlsx')

    :param data:
    :param filename:
    :return:
    """
    folder = 'Excel_Files'
    x = os.path.dirname(os.getcwd())
    y = os.path.join(x, folder)
    if not os.path.exists(y):
        os.makedirs(y)
    path = os.path.join(y, filename)
    all_data = pd.DataFrame(data)
    all_data.to_excel(path, index=False)


class Xpath:
    """
    Example usage:

    webpage = Xpath('https://www.example.com')

    webpage.fetch_page()
    """

    def __init__(self, url):
        self.url = url
        self.response = None
        self.soup = None

    def fetch_page(self):
        """
        Checking the Site is reachable or not reachable.
        :return:
        """
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
        else:
            print("failed to get page")

    def fame_xpath_generator(self):
        """
        This method Generates Xpath for 'a', 'span', 'input', 'button' tags present in the site.
        :return:
        """
        tags = self.soup.body.find_all()
        xpath_list = []
        no_duplicates = []
        for tag in tags:
            temp = {}
            if tag.text not in no_duplicates:
                if tag.name == 'a' and tag.text:
                    xp = "//" + f'{tag.name}' + '[normalize-space()=' + f'"{tag.text}"' + ']'
                    temp['Name'] = f'link_'+tag.text[:15]
                    temp['XPATH'] = xp
                    xpath_list.append(temp)
                    no_duplicates.append(tag.text)

                elif tag.name == 'span' and tag.text:
                    class_value = tag.get('class')
                    if class_value:
                        class_value = ' '.join(class_value)
                        xp = f"//{tag.name}[@class='{class_value}' and contains(text(), '{tag.text}')]"
                        temp['Name'] = 'span_'+tag.text[:15]
                        temp['XPATH'] = xp
                        xpath_list.append(temp)
                        no_duplicates.append(tag.text)

                elif tag.name == 'input':
                    xpath = '//'
                    xpath += tag.name + "["
                    attributes = tag.attrs
                    for attr, value in attributes.items():
                        if attr != 'class':
                            xpath += f'@{attr}="{value}" and '
                    xpath = xpath[:-5] + ']'
                    try:
                        temp['Name'] = "Input_" + f"{tag['placeholder']}"
                    except:
                        temp['Name'] = "Input" + f"{tag['name']}"
                    temp['XPATH'] = xpath
                    xpath_list.append(temp)
                    no_duplicates.append(tag.text)

                elif tag.name == 'button' and len(tag.text) != 0:
                    xp = "//" + f"{tag.name}" + '[.=' + f"'{tag.text}']"
                    temp['Name'] = 'button_'+tag.text[:15]
                    temp['XPATH'] = xp
                    xpath_list.append(temp)
                    no_duplicates.append(tag.text)

            else:
                continue
        return xpath_list

    def xpath_by_tag(self, tag_name):
        """
        Use this method to get xpath for any tag present in the site by providing tag name as param.

        Example Usage:

        xpath_by_tag('span').
        :param tag_name:
        :return:
        """
        tags = self.soup.body.find_all(tag_name)
        xpath_list = []
        no_duplicates = []
        for tag in tags:
            temp = {}
            if tag.text not in no_duplicates:
                if tag.name == tag_name and tag.text:
                    try:
                        xp = f'//{tag.name}'
                        if tag.attrs:
                            xp += '['
                            for attr, value in tag.attrs.items():
                                if attr == 'class':
                                    value = ' '.join(value)
                                xp += f"@{attr}='{value}' and "
                            xp = xp[:-5] + ']'
                        try:
                            temp['Name'] = "Input_" + f"{tag['placeholder']}"
                        except:
                            temp['Name'] = "Input" + f"{tag['name']}"
                        temp['XPATH'] = xp
                        xpath_list.append(temp)
                        no_duplicates.append(tag.text)
                    except:
                        xp = "//" + f'{tag.name}' + '[normalize-space()=' + f'"{tag.text}"' + ']'
                        temp['Name'] = f'{tag.name}_' + tag.text[:15]
                        temp['XPATH'] = xp
                        xpath_list.append(temp)
                        no_duplicates.append(tag.text)
        return xpath_list
