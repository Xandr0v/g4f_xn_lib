def read(src):
    with open(src, 'a+', encoding='utf-8') as f:
        f.seek(0)
        return f.read()


def write(data, src):
    with open(src, 'w', encoding='utf-8') as f:
        print(data, file=f)


def cut(s, vsc=100):
    if len(s) > vsc:
        s = f'{s[:vsc]}...'
    return s


def log(s, vsc):
    print(cut(s, vsc))
