def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))




# пример 1 - почему функция - это объект

# def get_russian_names():
#     return ['Ваня'], ['Коля'], ['Маша']
#
# def get_british_names():
#     return ['Oliver', 'Jack', 'Harry']
#
# name_getters = [get_russian_names, get_british_names]
#
# for name_getter in name_getters:
#     print(name_getter())

# пример 4 - функции, принимающие на вход другие функции с аргументами

# def adder(args):
#     res = 0
#     for number in args:
#         res += number
#     return res
#
# def multiplier(args):
#     res = 1
#     for number in args:
#         res *= number
#         print(res)
#     return res
#
# def process_numbers(numbers, function):
#     result = function(numbers)
#     print(f'Получилось {result}')
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# process_numbers(numbers=my_numbers, function=adder)
# process_numbers(numbers=my_numbers, function=multiplier)

# adder(my_numbers)
# print(adder(my_numbers))
#
# multiplier(my_numbers)
# print(multiplier(my_numbers))

# Пример 5 - функция map
# def mul_by_2(x):
#     return x * 2
#
# my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
#
# result = map(mul_by_2, my_numbers)
# print(result)
# print(list(result))