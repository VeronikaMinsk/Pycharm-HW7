def create_files(file_nums: str, file_psew: str, file_res: str):
    with (
        open(file_nums, 'r', encoding='utf-8') as f_nums,
        open(file_psew, 'r', encoding='utf-8') as f_psew,
        open(file_res, 'w', encoding='utf-8') as f_res
    ):
        f_psew_len = len(f_psew.readlines())
        f_nums_len = len(f_nums.readlines())

        f_nums.seek(0)
        f_psew.seek(0)

        for i in range(0, max(f_nums_len, f_psew_len)):
            spam = f_nums.readline().strip()
            eggs = f_psew.readline().strip()

            if not spam:
                f_nums.seek(0)
                spam = f_nums.readline().strip()
            if not eggs:
                f_psew.seek(0)
                eggs = f_psew.readline().strip()

            curr_list = spam.split('|')
            mult = int(curr_list[0]) * float(curr_list[1])

            f_res.write(f'{eggs.lower()} {abs(mult)}\n' if mult < 0 else f'{eggs.upper()} {round(mult)}\n')
