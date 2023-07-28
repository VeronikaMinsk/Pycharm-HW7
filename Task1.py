# Задание №5
# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.


import os
from Func_Pac import generate_files_with_extensions


# MIN_LEN_NAME = 6
# MAX_LEN_NAME = 30
# MIN_SIZE = 256
# MAX_SIZE = 4096
# STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'


# def create_random_files(output_folder, exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, max_size=MAX_SIZE,
#                 count_file=1):
#     for _ in range(0, count_file):
#         name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
#         file_path = os.path.join(output_folder, name_file)
#
#         with open(file_path, 'wb') as f:
#             f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))
#
#
# def generate_files(output_folder, extensions_and_counts):
#     for ext, count in extensions_and_counts:
#         create_random_files(output_folder, ext, count_file=count)


if __name__ == '__main__':

    extensions_and_counts = [('txt', 5), ('csv', 3), ('json', 2), ('bin', 3)]
    output_folder = 'Task1_archive'
    os.makedirs(output_folder, exist_ok=True)
    generate_files_with_extensions(output_folder, extensions_and_counts)

