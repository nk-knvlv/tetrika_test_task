import requests
from bs4 import BeautifulSoup
import csv


def write_dict_into_csv(target_dict: dict, filename: str):
    with open(filename, 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for name in target_dict:
            writer.writerow([name, target_dict[name]])


def get_wiki_beasts():
    beasts = {}

    site = "https://ru.wikipedia.org"
    url = site + "/w/index.php"
    params = {
        "title": "Категория:Животные_по_алфавиту",
    }

    while url:
        # Отправляем HTTP-запрос и получаем ответ
        response = requests.get(url, params=params)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'lxml')

            beasts_section = soup.find('div', class_='mw-category-generated').find('div', id='mw-pages')
            beast_categories = beasts_section.find_all('div', class_='mw-category-group')
            for beasts_list in beast_categories:
                category_letter = beasts_list.find('h3').get_text()
                if category_letter not in beasts:
                    beasts[category_letter] = 0
                beasts[category_letter] += len(beasts_list.find_all('li'))

            if next_page_btn := beasts_section.find('a', text='Следующая страница'):
                url = site + next_page_btn['href']
            else:
                url = None
        else:
            print("Ошибка получения страницы")
    filename = 'beasts.csv'
    write_dict_into_csv(beasts, filename)
