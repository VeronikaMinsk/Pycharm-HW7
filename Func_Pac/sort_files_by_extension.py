import os
import shutil

def sort_files_by_extension(source_folder):
    extensions_by_group = {
        'video': ('mp4', 'avi', 'mkv'),
        'images': ('jpg', 'jpeg', 'png', 'gif'),
        'text': ('txt', 'csv', 'json', 'xml'),

    }

    for filename in os.listdir(source_folder):
        if os.path.isfile(os.path.join(source_folder, filename)):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()[1:]

            target_group = None
            for group, exts in extensions_by_group.items():
                if ext in exts:
                    target_group = group
                    break

            if target_group is not None:
                target_folder = os.path.join(source_folder, target_group)
                os.makedirs(target_folder, exist_ok=True)

                source_file = os.path.join(source_folder, filename)
                target_file = os.path.join(target_folder, filename)

                shutil.move(source_file, target_file)
            else:
                print(f"Файл '{filename}' не подошел для сортировки и оставлен в исходной папке.")
    pass
