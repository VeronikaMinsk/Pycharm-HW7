from .create_random_files import create_random_files

def generate_files_with_extensions(output_folder, extensions_and_counts):
    for ext, count in extensions_and_counts:
        create_random_files(output_folder, ext, count_file=count)
