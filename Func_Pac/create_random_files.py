import os
import random
from random import randint


MIN_LEN_NAME = 6
MAX_LEN_NAME = 30
MIN_SIZE = 256
MAX_SIZE = 4096
COUNT_FILE = 42
STR_CHAR = 'qwrtpsdfghjklzxcvbnm'

def create_random_files(output_folder, exp: str, min_len_name=MIN_LEN_NAME, max_len_name=MAX_LEN_NAME, min_size=MIN_SIZE, max_size=MAX_SIZE,
                count_file=COUNT_FILE):
    for _ in range(count_file):
        name_file = "".join(random.choices(STR_CHAR, k=random.randint(min_len_name, max_len_name))) + '.' + exp
        file_path = os.path.join(output_folder, name_file)

        with open(file_path, 'wb') as f:
            f.write(bytes(randint(0, 255) for _ in range(randint(min_size, max_size))))




