import random

STR_CHAR = 'qwrtpsdfghjklzxcvbnm'
STR_VOWEL = 'eyuioa'
MIN_LEN_PS = 4
MAX_LEN_PS = 7

def gen_psevdonim(name_file: str):
    spam = random.sample(STR_CHAR, random.randint(MIN_LEN_PS, MAX_LEN_PS - 1))
    eggs = random.sample(STR_VOWEL, random.randint(1, len(STR_VOWEL)))
    eggs.extend(spam)
    eggs = eggs[:random.randint(MIN_LEN_PS, MAX_LEN_PS)]
    random.shuffle(eggs)
    print(eggs)
    with open(name_file, 'a', encoding='utf-8') as f:
        f.write(f'{"".join(eggs).title()}\n')
