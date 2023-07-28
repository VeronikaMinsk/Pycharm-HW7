# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import os
from Func_Pac import generate_files_with_extensions

# import random
# from random import randint
#
# MIN_LEN_NAME = 6
# MAX_LEN_NAME = 30
# MIN_SIZE = 256
# MAX_SIZE = 4096
# STR_CHAR = 'qwrtpsdfghjklzxcvbnmeyuioa'
#
#
# def create_file(output_folder, exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, max_size=MAX_SIZE,
#                 count_file=1):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     existing_files = set(os.listdir(output_folder))
#
#     for _ in range(count_file):
#         name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
#
#         while name_file in existing_files:
#             name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
#
#         file_path = os.path.join(output_folder, name_file)
#         existing_files.add(name_file)
#
#         if not os.path.exists(file_path):
#             with open(file_path, 'wb') as f:
#                 f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))
#
#
# def generate_files_with_extensions(output_folder, extensions_and_counts):
#     for ext, count in extensions_and_counts:
#         create_file(output_folder, ext, count_file=count)


if __name__ == '__main__':
    extensions_and_counts = [('', 3), ('csv', 5), ('json', 2), ('bin', 4)]
    output_folder = 'Task2_archive'
    os.makedirs(output_folder, exist_ok=True)
    generate_files_with_extensions(output_folder, extensions_and_counts)
