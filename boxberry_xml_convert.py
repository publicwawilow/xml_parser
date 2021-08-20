from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import csv
from difflib import SequenceMatcher


from icecream import ic


def same_text_or_not(text_one, text_two, similarity_kaf=0.9):
    try:
        text_one = str(text_one)
        text_two = str(text_two)
    except:
        return False
    similarity = SequenceMatcher(None, text_one, text_two).ratio()
    if similarity >= similarity_kaf:
        return True
    else:
        return False


def what_is_it(inf, kaf=0.9):
    csv_table = []
    with open('2_5460663850116321236.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            csv_table.append(row[0].split(';'))
    for i in csv_table:
        if same_text_or_not(i[0], str(inf), similarity_kaf=kaf):
            if i[-3] == '"Бренд"':
                return ['brand', i[0]]
            if i[-3] == '"Размер"':
                return ['size', i[0]]
            if i[-3] == '"Тип одежды (для размеров)"':
                return ['size', i[0]]
            if i[-3] == '"Серия"':
                return ['series', i[0]]
            if i[-3] == '"Страна"':
                return ['country', i[0]]
            if i[-3] == '"Цвет"':
                return ['color', i[0]]
    return None


def make_xml_file(table_name, list):
    print('make xml')
    table = ET.Element('Товар')
    for i in range(len(list)):
        product_name = list[0]
        id = list[1]
        maker_code = list[2]
        brand, size, country, color = False, False, False, False
        print('what is it')
        for i in list[3:]:
            what = what_is_it(i, 0.8)
            if what == None:
                pass
            elif what[0] == 'brand':
                brand = what[1]
            elif what[0] == 'size':
                size = what[1]
            elif what[0] == 'series':
                pass
            elif what[0] == 'country':
                country = what[1]
            elif what[0] == 'color':
                color = what[1]
        print('found what is it')
        product = ET.SubElement(table, 'Наименование')
        product.text = f"{product_name}"
        data = ET.SubElement(table, 'ХарактеристикиТовара')

        element1 = ET.SubElement(data, 'ХарактеристикаТовара')
        s_elem1 = ET.SubElement(element1, 'Ид')
        s_elem2 = ET.SubElement(element1, 'Наименование')
        s_elem3 = ET.SubElement(element1, 'Значение')

        s_elem1.text = f"{id}"
        s_elem2.text = "КОД ПРОИЗВОДИТЕЛЯ"
        s_elem3.text = f"{maker_code}"

        if brand:
            elem_brand = ET.SubElement(data, 'ХарактеристикаТовара')
            s_brand = ET.SubElement(elem_brand, 'Наименование')
            s_brand2 = ET.SubElement(elem_brand, 'Значение')

            s_brand.text = "БРЕНД"
            s_brand2.text = f"{brand}"

        if size:
            elem_brand = ET.SubElement(data, 'ХарактеристикаТовара')
            s_brand = ET.SubElement(elem_brand, 'Наименование')
            s_brand2 = ET.SubElement(elem_brand, 'Значение')

            s_brand.text = "РАЗМЕР"
            s_brand2.text = f"{size}"

        if country:
            elem_brand = ET.SubElement(data, 'ХарактеристикаТовара')
            s_brand = ET.SubElement(elem_brand, 'Наименование')
            s_brand2 = ET.SubElement(elem_brand, 'Значение')

            s_brand.text = "СТРАНА"
            s_brand2.text = f"{country}"

        if color:
            elem_brand = ET.SubElement(data, 'ХарактеристикаТовара')
            s_brand = ET.SubElement(elem_brand, 'Наименование')
            s_brand2 = ET.SubElement(elem_brand, 'Значение')

            s_brand.text = "Цвет"
            s_brand2.text = f"{color}"

        tree = ET.ElementTree(table)
        print('num', i)

    with open(f"{table_name}.xml", "wb") as f:
        tree.write(f, encoding='utf-8')


def one_item_xml_parse(file_name, suggestion_num):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    print('reading ok')
    xml_data = BeautifulSoup(data, 'xml')
    print('convert ok')
    suggestions = xml_data.find_all('Предложение')
    id = str(suggestions[suggestion_num].find('Ид')).split('Ид')[1][1:][:-2]
        # here i have big <Наименование>
        # with structure Name (maker_id, brand, size)
    suggestions_name = str(suggestions[suggestion_num].find('Наименование')).split('Наименование')[1][1:][:-2]
        # convert str {Носки Asics 3PPK Lyte Sock (3 пары) (123458 0900-I, Asics, 3 пары, 35-38, Турция, черно-серый)}
        # to list
    inf_list = suggestions_name.split(', ')
    inf = inf_list[1:]
    product_name = inf_list[0]
    maker_code = product_name.split('(')[-1]
    product_name = "(".join(product_name.split('(')[:-1])
    return suggestions_name, id


def xml_parse(file_name):
    with open(f"{file_name}.xml", 'r', encoding='utf-8') as f:
        data = f.read()
    print('reading ok')
    xml_data = BeautifulSoup(data, 'xml')
    print('convert ok')
    suggestions = xml_data.find_all('Предложение')
    list = []
    len_inf = []
    for suggestion_num in range(len(suggestions)):
        id = str(suggestions[suggestion_num].find('Ид')).split('Ид')[1][1:][:-2]
        # here i have big <Наименование>
        # with structure Name (maker_id, brand, size)
        suggestions_name = str(suggestions[suggestion_num].find('Наименование')).split('Наименование')[1][1:][:-2]
        # convert str {Носки Asics 3PPK Lyte Sock (3 пары) (123458 0900-I, Asics, 3 пары, 35-38, Турция, черно-серый)}
        # to list
        inf_list = suggestions_name.split(', ')
        inf = inf_list[1:]
        product_name = inf_list[0]
        maker_code = product_name.split('(')[-1]
        product_name = "(".join(product_name.split('(')[:-1])

        list.append([product_name, id, maker_code, *inf])
        # len_inf.append([[len(inf), suggestion_num, product_name, id, maker_code, *inf]])
    # return len_inf
    return list


if __name__ == '__main__':
    print()
    # print(one_item_xml_parse('2_5460663850116321203.xml', suggestion_num=99))
    a = xml_parse('2_5460663850116321203.xml')
    N = len(a)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
