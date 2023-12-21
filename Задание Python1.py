


#Чтение строки
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
        index = index+n
        n += 2
    return combined_list




# Сжатие строки
def compression(st):
    if len(st)<4 or len(st)%4 != 0:
        return st
    st = st[::-1]
    lst = split_string(st)
    lst = combine_digits(lst)
    for i in range(len(lst)):
        if lst[i].count(lst[i][0]) == 4:
            lst[i] = lst[i][0]
    result = ''.join(lst)
    return result[::-1]


# финальное сжатие
def fin_compression(result):
    while len(result) >= 4 or len(result)%4 == 0:
        result = compression(result)
    return result




# Запись в строку
with open("output.txt", "w") as file2:
    file2.write(fin_compression(str1))
