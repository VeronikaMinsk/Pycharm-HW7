
from Func_Pac import add_number

MIN_NUM = -1000
MAX_NUM = 1000


# def add_number(count: int, name_file: str):
#     with open(name_file, 'a', encoding='utf-8') as f:
#         for i in range(0, count):
#             f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    add_number(5, 'task01.txt')

