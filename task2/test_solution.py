from solution import get_wiki_beasts
import pytest
import os
import csv


def test_get_wiki_beasts():
    file_path = "beasts.csv"
    assert os.path.exists(file_path) is False
    get_wiki_beasts()
    assert os.path.exists(file_path) is True
    assert os.stat("beasts.csv").st_size is not 0

    with open('beasts.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 3:  # проверяем индекс строки
                print(row)  # выводим 4 строчку
                assert row[0] == 'Г'
                break  # выходим из цикла после вывода 4 строчки

