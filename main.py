# 6 hours work 30 minutes
import csv
from difflib import SequenceMatcher
from boxberry_xml_convert import *

from icecream import ic


def same_text_or_not(text_one, text_two, similarity_kaf=0.9):
    similarity = SequenceMatcher(None, text_one, text_two).ratio()
    if similarity >= similarity_kaf:
        return True
    else:
        return False


def what_is_it(inf):
    csv_table = []
    with open('2_5460663850116321236.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_table.append(row[0].split(';'))
    for i in csv_table:
        print(str(inf))
        if same_text_or_not(i[0], str(inf), similarity_kaf=0.9):
            if i == '"Бренд"':
                return ['brand', i[0]]
            if i == '"Размер"':
                return ['size', i[0]]
            if i == '"Серия"':
                return ['series', i[0]]
            if i == '"Страна"':
                return ['country', i[0]]
            if i == '"Тип одежды (для размеров)"':
                return ['type', i[0]]
            if i == '"Цвет"':
                return ['color', i[0]]
    return None



if __name__ == '__main__':
    name = "Сумка Hayabusa Ryoko Mesh Gear Bag (RYMGB-B70, Hayabusa, Китай , черно-серый)"
    print(what_is_it('Китай'))
    inf = ['RYMGB-B70', 'Hayabusa', 'Китай', 'черно-серый']
    for i in inf:
        print(what_is_it(i))
