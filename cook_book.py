def get_indigrients(file_name):
    cook_book = {}
    with open(file_name, encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            count = int(file.readline().strip())
            list_dish = []
            for indigrients in range(count):
                ingredient_name, quantity, measure = file.readline().split('|')
                sostav =  {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                list_dish.append(sostav)
            cook_book[name] = list_dish
            file.readline()
            print(line)
    return cook_book
result = get_indigrients('text.txt')
print(result)