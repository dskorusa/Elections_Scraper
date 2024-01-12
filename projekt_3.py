# head
"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: David Skoruša
email: d.skorusa@post.cz
discord: David Skoruša#7746
"""

# Toto je verze, která mi scrapuje pouze kód obce a jméno obce, bohužel se mi nepodařilo přijít, jak na to další.
# V dalším souboru je tento kód upraven a rozšířen, o ty věci, které by se měly dále scrapovat, ale nedaří se mi to.
# Chci však mít kód uložen pro případnou další práci. Prosím, podívej se na tento i ten druhý kód, díky.

import csv
import sys
import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error: Unable to retrieve HTML content from {url}")
        return None

def parse_html(html, parser_type='html.parser'):
    soup = BeautifulSoup(html, parser_type)
    return soup

def get_main_attributes_1(html_soup):
    main_attributes = []
    for tr_tag in html_soup.select('tr'):
        name_element = tr_tag.find('td', {'headers': 't1sa1 t1sb2'})
        number_element = tr_tag.find('td', {'class': 'cislo'})


        if name_element and number_element:
            name = name_element.text.strip()
            number = number_element.text.strip()
            main_attributes.append({'name': name, 'number': number})

    return main_attributes

def get_main_attributes_2(html_soup):
    main_attributes = []
    for tr_tag in html_soup.select('tr'):
        name_element = tr_tag.find('td', {'headers': 't2sa1 t2sb2'})
        number_element = tr_tag.find('td', {'class': 'cislo'})
        district_element = tr_tag.find('td', {'class': ''})


        if name_element and number_element:
            name = name_element.text.strip()
            number = number_element.text.strip()
            main_attributes.append({'name': name, 'number': number})

    return main_attributes

def get_main_attributes_3(html_soup):
    main_attributes = []
    for tr_tag in html_soup.select('tr'):
        name_element = tr_tag.find('td', {'headers': 't3sa1 t3sb2'})
        number_element = tr_tag.find('td', {'class': 'cislo'})


        if name_element and number_element:
            name = name_element.text.strip()
            number = number_element.text.strip()
            main_attributes.append({'name': name, 'number': number})

    return main_attributes

def get_municipality_url(html_soup):
    municipality_url = []
    tables = html_soup.find_all("td", class_="cislo")
    for table in tables:
        link = table.find("a")
        url = link["href"]
        municipality_url.append({'url': url})

    return municipality_url


url = 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7103'
html_content = get_html(url)

if html_content:
    parsed_html = parse_html(html_content)
    main_attributes_1 = get_main_attributes_1(parsed_html)
    main_attributes_2 = get_main_attributes_2(parsed_html)
    main_attributes_3 = get_main_attributes_3(parsed_html)
    municipality_url = get_municipality_url(parsed_html)


    # Writing to CSV file
    csv_file_path = 'vysledky_prostejov.csv'
    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        fieldnames = ['name', 'number','url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        for attribute in main_attributes_1:
            writer.writerow(attribute)

        for attribute in main_attributes_2:
            writer.writerow(attribute)

        for attribute in main_attributes_3:
            writer.writerow(attribute)

        for attribute in municipality_url:
            writer.writerow(attribute)


    print(f'Data has been written to {csv_file_path}')

