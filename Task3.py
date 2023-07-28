# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from Func_Pac import sort_files_by_extension
import os
import shutil

# def sort_files_by_extension(source_folder):
#     extensions_by_group = {
#         'video': ('mp4', 'avi', 'mkv'),
#         'images': ('jpg', 'jpeg', 'png', 'gif'),
#         'text': ('txt', 'csv', 'json', 'xml'),
#
#     }
#
#     for filename in os.listdir(source_folder):
#         if os.path.isfile(os.path.join(source_folder, filename)):
#             _, ext = os.path.splitext(filename)
#             ext = ext.lower()[1:]
#
#
#             target_group = None
#             for group, exts in extensions_by_group.items():
#                 if ext in exts:
#                     target_group = group
#                     break
#
#             if target_group is not None:
#                 target_folder = os.path.join(source_folder, target_group)
#                 os.makedirs(target_folder, exist_ok=True)
#
#                 source_file = os.path.join(source_folder, filename)
#                 target_file = os.path.join(target_folder, filename)
#
#                 shutil.move(source_file, target_file)
#             else:
#                 print(f"Файл '{filename}' не подошел для сортировки и оставлен в исходной папке.")

if __name__ == '__main__':
    source_folder = 'Task3_archive'
    sort_files_by_extension(source_folder)

