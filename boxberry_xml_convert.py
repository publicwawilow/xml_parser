from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


def make_xml_file(table_name, list):
    table = ET.Element('Товар')
    for i in range(len(list)):
        product_name, id, maker_code, brand, size, country, color = list[i]
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
    return suggestions_name


def xml_parse(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        data = f.read()
    print('reading ok')
    xml_data = BeautifulSoup(data, 'xml')
    print('convert ok')
    suggestions = xml_data.find_all('Предложение')
    list = []
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
    return list


if __name__ == '__main__':
    print()
    # print(one_item_xml_parse('2_5460663850116321203.xml', suggestion_num=99))
    print(xml_parse('2_5460663850116321203.xml'))