# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

from Func_Pac import create_random_files
import os



# def create_random_files(output_folder, exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, max_size=MAX_SIZE,
#                 count_file=COUNT_FILE):
#     for _ in range(count_file):
#         name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
#         file_path = os.path.join(output_folder, name_file)
#
#         with open(file_path, 'wb') as f:
#             f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))


if __name__ == '__main__':
    output_folder = 'Sem4-archive'
    os.makedirs(output_folder, exist_ok=True)

    create_random_files(output_folder, 'txt', count_file=3)
