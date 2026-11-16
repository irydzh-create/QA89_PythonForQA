def is_valid_point(point):  # создаём функцию с параметром point

    if point is None:  # если point равен None
        return None  # возвращаем None и завершаем функцию

    if isinstance(point, tuple) and len(point) == 0:
        # isinstance(point, tuple) — проверяем, является ли point кортежем
        # and — И, оба условия должны выполняться
        # len(point) == 0 — количество элементов равно нулю
        return None  # возвращаем None

    if not isinstance(point, tuple) or len(point) != 2:
        # not isinstance(point, tuple) — point НЕ является кортежем
        # or — ИЛИ, достаточно одного выполненного условия
        # len(point) != 2 — количество элементов НЕ равно двум
        return False  # возвращаем False

    x, y = point  # распаковываем кортеж: x — первый, y — второй элемент

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        # not isinstance(x, (int, float)) — x НЕ является int или float
        # or — ИЛИ
        # not isinstance(y, (int, float)) — y НЕ является int или float
        return False  # возвращаем False

    return True  # все проверки пройдены, возвращаем True
# def is_valid_point(point):
#     if point is None:
#         return None
#     if isinstance(point, tuple) and len(point) == 0:
#         return None
#     if not isinstance(point, tuple): #or len(point) != 2:
#         return False
#     if len(point) != 2:
#         return False
#     x,y = point
#     if not isinstance(x(int,float)) or not isinstance(y,(int,float)):
#         return False
#     return True