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

def get_voters(html_soup):
    number_voters_for_one_town = []
    tables = html_soup.find_all("th", id="sa2")
    for table in tables:
        link = table.find("a")
        url = link["href"]


    return number_voters_for_one_town
def get_envelopes_issued(html_soup):
    number_envelopes_issued_for_one_town = []
    tables = html_soup.find_all("th", id="sa3")
    for table in tables:
        link = table.find("a")
        url = link["href"]
        number_envelopes_issued_for_one_town.append({'number_envelopes_issued_for_one_town': number_envelopes_issued_for_one_town})

    return number_envelopes_issued_for_one_town
def get_valid_votes(html_soup):
    number_valid_votes_for_one_town_for_one_town = []
    tables = html_soup.find_all("th", id="sa6")
    for table in tables:
        link = table.find("a")
        url = link["href"]
        number_valid_votes_for_one_town.append({'number_valid_votes_for_one_town': number_valid_votes_for_one_town})

    return number_valid_votes_for_one_town
def get_candidate_parties(html_soup):
    number_candidate_parties_for_one_town = []
    tables = html_soup.find_all('td', {'class': 'overflow_name'})
    for table in tables:
        link = table.find("a")
        url = link["href"]
        number_candidate_parties_for_one_town.append({'number_candidate_parties_for_one_town': number_candidate_parties_for_one_town})

    return number_valid_votes_for_one_town


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


        for town_url in municipality_url:
            town_url = 'https://volby.cz/pls/ps2017nss/' + town_url['url']
            html_content = get_html(town_url)
            if html_content:
                html_soup = parsed_html(html_content)
                number_voters_for_one_town = get_voters(_html_soup)
                number_envelopes_issued_for_one_town = get_envelopes_issued(_html_soup)
                number_valid_votes_for_one_town = get_valid_votes(_html_soup)
                number_candidate_parties_for_one_town = get_candidate_parties(_html_soup)

    print(f'Data has been written to {csv_file_path}')

