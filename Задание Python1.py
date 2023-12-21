#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

#Чтение файла
with open("input.txt", "r") as file:
    str1 = file.readline()

# Делим строку по комбинациям 1 и 3 элемента
def split_string(string):
    split_list = []
    is_single = True
    current_string = ""

    for char in string:
        if is_single:
            split_list.append(char)
            is_single = False
        else:
            current_string += char
            if len(current_string) == 3:
                split_list.append(current_string)
                current_string = ""
                is_single = True

    if current_string:
        split_list.append(current_string)

    return split_list


# Объединям по треугольникам
def combine_digits(lst):
    combined_list = []
    n = 1
    index = 0
    while index < len(lst):
        k = n
        while k != 0 :
            combined_list.append(lst[index]+lst[index+n])
            k -=1
            index += 1
        index = index + n
        n += 2
    return combined_list



# Сжатие строки
def compression(st):
    var = 0
    if len(st) < 4 or len(st)%4 != 0:
        return st, var
    st = st[::-1]
    lst = split_string(st)
    lst = combine_digits(lst)
    for i in range(len(lst)):
        if lst[i].count(lst[i][0]) == 4:
            lst[i] = lst[i][0]
    result = ''.join(lst)
    if sorted(result) == sorted(st):
        var = 1
        return st[::-1], var
    return result[::-1], var


# финальное сжатие
def fin_compression(result):
    while len(result) > 4:
        result, var = compression(result)
        if var == 1:
            return result
    if len(result) == 4:
        result, var = compression(result)
    return result


# Запись в файл
with open("output.txt", "w") as file2:
    file2.write(fin_compression(str1))
