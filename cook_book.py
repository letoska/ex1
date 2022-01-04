def get_indigrients(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            count = int(file.readline().strip())
            list_dish = []
            for indigrients in range(count):
                ingredient_name, quantity, measure = file.readline().split('|')
                sostav = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                list_dish.append(sostav)
            cook_book[name] = list_dish
            file.readline()
            print(line)
    return cook_book


result = get_indigrients('text.txt')
print(result)


def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish, sostav in result.items():
        if dish in dishes:
            for indigrients in sostav:
                i_n = list(indigrients.values())[0]
                q = (int(list(indigrients.values())[1]) * person_count)
                m = list(indigrients.values())[2]
                if dishes[0] == dishes[1]:
                    order[i_n] = {'measure': q * 2, 'quantity': m}
                else:
                    order[i_n] = {'measure': q, 'quantity': m}
    print(order)


get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
