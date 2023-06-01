def filter_capitalized_strings(string_list):
    filtered_list = []
    for string in string_list:
        if string[0].isupper():
            filtered_list.append(string)
            return filtered_list
            input_list = input("Введіть список рядків (розділених пробілами): ").split()
            filtered_strings = filter_capitalized_strings(input_list)
            print("Результат:", filtered_strings)

