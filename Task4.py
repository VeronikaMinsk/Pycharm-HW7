# 2.Напишите функцию группового переименования файлов. Она должна:
# * -- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# * -- принимать параметр количество цифр в порядковом номере.
# * -- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# * -- принимать параметр расширение конечного файла.
# * -- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

from Func_Pac import rename_files_in_directory

# def rename_files_in_directory(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
#     counter = 1
#     source_extension = source_extension.lower()
#     target_extension = target_extension.lower()
#
#     for filename in os.listdir(directory):
#         file_path = os.path.join(directory, filename)
#
#         if os.path.isfile(file_path) and filename.lower().endswith(f".{source_extension}"):
#             source_name = filename[:-len(source_extension) - 1]
#             source_name_range = slice(*name_range) if name_range else slice(None)
#
#             new_name = (
#                 source_name[source_name_range] +
#                 desired_name +
#                 str(counter).zfill(num_digits) +
#                 f".{target_extension}"
#             )
#
#             counter += 1
#
#             new_file_path = os.path.join(directory, new_name)
#             os.rename(file_path, new_file_path)
#             print(f"Переименовано: {filename} -> {new_name}")

if __name__ == '__main__':
    directory = 'Task1_archive'
    desired_name = 'new_file'
    num_digits = 3
    source_extension = 'txt'
    target_extension = 'docx'
    name_range = (3, 6)

    rename_files_in_directory(directory, desired_name, num_digits, source_extension, target_extension, name_range)
