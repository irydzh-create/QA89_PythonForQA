# #zadanie1
# def print_list_reverse(lst):
#     if lst is None or not isinstance(lst, list) or len(lst) == 0:
#         print("Wrong list")
#         return
#     reversed_lst = lst[::-1]
#     print(reversed_lst)
# print_list_reverse([1, 2, 3, 4, 5])
# print_list_reverse([])
# print()

# Задание 1

def print_list_reverse(lst):  # создаём функцию с параметром lst (список)

    if lst is None or not isinstance(lst, list) or len(lst) == 0:
        # lst is None — проверяем, равен ли lst значению None
        # or — ИЛИ, достаточно выполнения одного условия
        # not isinstance(lst, list) — lst НЕ является списком (list)
        # or — ИЛИ
        # len(lst) == 0 — проверяем, пустой ли список (0 элементов)

        print("Wrong list")  # выводим сообщение Wrong list в консоль
        return  # завершаем функцию, дальнейший код не выполняется

    reversed_lst = lst[::-1]
    # reversed_lst — переменная для хранения перевёрнутого списка
    # lst[::-1] — создаём новый список с элементами в обратном порядке
    # [start:stop:step] — формат среза списка
    # step = -1 — двигаемся по списку с конца к началу

    print(reversed_lst)  # выводим перевёрнутый список в консоль


# ТЕСТЫ

print_list_reverse([1, 2, 3, 4, 5])  # вывод: [5, 4, 3, 2, 1]

print_list_reverse([])  # вывод: Wrong list, потому что список пустой

print()  # выводим пустую строку (переход на новую строку)