# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc

letters = open('string_to_compress.txt', 'r')
my_dict = {}
letters_list = []
for line in letters:
    letters_list = line

for letter in letters_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1

my_list = []
for letter, count in my_dict.items():
    my_list.append(count)
    my_list.append(letter)

for i in range(len(my_list)):
    my_list[i] = str(my_list[i])

with open('compressed_string.txt', 'w') as output_count:
    output_count.write(''.join(my_list))

letters.close()

compressed_string = open('compressed_string.txt', 'r')
for line in compressed_string:
    letters_count = line

recovered_string = ''
for i in range(len(letters_count)):
    if letters_count[i].isdigit():
        recovered_string = recovered_string + str(letters_count[i+1]) * int(letters_count[i])

with open('recovered_string.txt', 'w') as out_rec_string:
    out_rec_string.write(recovered_string)

compressed_string.close()