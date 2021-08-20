# 3 hours work 20 minutes
import xml.etree.ElementTree as ET


def make_xml_file(table_name, product_name, id, maker_code, brand, size, country, color):
    table = ET.Element('Товар')
    for i in range(10):
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


if __name__ == '__main__':
    make_xml_file('table_name', 'product_name', 'id', 'maker_code', 'brand', 'size', 'country', 'color')

