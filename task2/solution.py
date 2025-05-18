import requests
import json
import pprint
from bs4 import BeautifulSoup

# URL API Википедии
url = "https://ru.wikipedia.org/w/index.php"

# Параметры запроса
params = {
    "title": "Категория:Животные_по_алфавиту",
}

# Отправляем HTTP-запрос и получаем ответ
response = requests.get(url, params=params)

# Проверяем, что ответ получен успешно
if response.status_code == 200:
    # Парсим ответ в JSON
    # pprint.pprint(response.text)
    #
    soup = BeautifulSoup(response.text, 'html.parser')

    generated_categories_div = soup.find('div', class_='mw-category-generated')
    animal_category_div = generated_categories_div.find('div', id='mw-pages')
    # ul = animal_category_div.find('ul')
    li_count = len(animal_category_div.find_all('li'))

    print(li_count)

else:
    print("Ошибка получения страницы")
