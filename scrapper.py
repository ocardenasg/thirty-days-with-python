import os
import datetime
import requests
import pandas as pd
from requests_html import HTML


def url_to_html(url, save=False):
    request = requests.get(url)

    if request.status_code != 200:
        print('something went wrong...')
        return ''

    html_text = request.text

    if save:
        with open(f"htmls/movies.html", 'w') as f:
            f.write(html_text)
    return html_text


def parse_movies_from_url(url):
    data = []
    headers = []

    html_txt = url_to_html(url)
    r_html = HTML(html=html_txt)
    r_table = r_html.find('#table')

    if len(r_table) > 0:
        parsed_table = r_table[0]
        rows = parsed_table.find('tr')
        headers = [header.text for header in rows[0].find('th')]
        for row in rows[1:]:
            columns = row.find('td')
            row_data = []
            for column in columns:
                row_data.append(column.text)
            data.append(row_data)
    return (headers, data)


def create_dataset_from_movies(url, dataset_name='dataset'):
    dataset = f"datasets/{dataset_name}.csv"

    headers, data = parse_movies_from_url(url)
    if len(headers) and len(data):
        data_frame = pd.DataFrame(data, columns=headers)
        data_frame.to_csv(dataset, index=False)


def get_dataset(to_year, from_year=1977):
    if (to_year < from_year):
        return True

    url = f"https://www.boxofficemojo.com/year/world/{to_year}"
    dataset_name = f"movies_{to_year}"
    create_dataset_from_movies(url, dataset_name)
    print(f"collected {to_year}")
    return get_dataset(to_year - 1, from_year)


if __name__ == "__main__":
    get_dataset(from_year=2015, to_year=2017)
