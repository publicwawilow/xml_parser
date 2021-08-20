def str_convert():
    a = 'Борцовки Matflex 5 Asics (J504N, 9093, Asics, 800, 46 (13 USA), Вьетнам, черно-серебряный)'
    b = 'Тайтсы женские Knee Tight Asics (134113, 0904-S, Asics, 200, S, Малайзия, черный)'
    c = 'Носки Asics 3PPK Lyte Sock (3 пары) (123458 0900-I, Asics, 3 пары, 35-38, Турция, черно-серый)'
    list = [a, b, c]
    for suggestions_name in list:
        inf_list = suggestions_name.split(', ')
        inf = inf_list[1:]
        product_name = inf_list[0]
        maker_code = product_name.split('(')[-1]
        product_name = "(".join(product_name.split('(')[:-1])

        print()
        print(inf)
        print(product_name)
        print(maker_code)