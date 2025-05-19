import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=Yacarerani#mw-pages'
li_count = 0
params = {
    "title": "Категория:Животные_по_алфавиту",
}
# Отправляем HTTP-запрос и получаем ответ
response = requests.get(url, params=params)
beasts = {}
if response.status_code == 200:
    # Отправляем HTTP-запрос и получаем ответ
    response = requests.get(url, params=params)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')

        beasts_section = soup.find('div', class_='mw-category-generated').find('div', id='mw-pages')
        beast_categories = beasts_section.find_all('div', class_='mw-category-group')
        beast_li_list = []
        for anim_list in beast_categories:
            category_letter = anim_list.find('h3').get_text()
            if category_letter not in beasts:
                beasts[category_letter] = 0
            beasts[category_letter] += len(anim_list.find_all('li'))
            print(category_letter)

        print(url)
        print(beasts)
        # # if next_page_btn := beasts_section.find('a', text='Следующая страница'):
        # #     url = site + next_page_btn['href']
        # else:
        #     url = None
    else:
        print("Ошибка получения страницы")