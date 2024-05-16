_file_limit = 100
def set_file_limit(n):
    global _file_limit
    _file_limit = n

def output(text, out_folder='./output', format='txt'):
    import re
    import os


    if not os.path.exists(out_folder):
        os.mkdir(out_folder)

    pat = re.compile(r'(?<=out)\d+(?=\.\w+)')

    files = os.listdir(out_folder)
    ms = (pat.search(file) for file in files)
    out_nums = sorted(int(m.group(0)) for m in ms if m is not None)
    if len(out_nums) == 0:
        out_nums = [1]
    else:
        out_nums.append(out_nums[-1] + 1)

    with open(f'{out_folder}/out{out_nums[-1]}.{format}', 'w', encoding='utf-8') as f:
        print(text, file=f)

    while len(out_nums) > _file_limit:
        os.remove(f'{out_folder}/out{out_nums[0]}.{format}')
        out_nums.pop(0)