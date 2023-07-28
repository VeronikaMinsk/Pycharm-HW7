import os

def rename_files_in_directory(directory, desired_name, num_digits, source_extension, target_extension, name_range=None):
    counter = 1
    source_extension = source_extension.lower()
    target_extension = target_extension.lower()

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path) and filename.lower().endswith(f".{source_extension}"):
            source_name = filename[:-len(source_extension) - 1]
            source_name_range = slice(*name_range) if name_range else slice(None)

            new_name = (
                source_name[source_name_range] +
                desired_name +
                str(counter).zfill(num_digits) +
                f".{target_extension}"
            )

            counter += 1

            new_file_path = os.path.join(directory, new_name)
            os.rename(file_path, new_file_path)
            print(f"Переименовано: {filename} -> {new_name}")
