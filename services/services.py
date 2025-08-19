from random import choice


# That function choice random quate
def choice_quate(quates: dict) -> str:
    return choice(list(quates.keys()))


# That function return dict of quates
def read_quates(path: str) -> dict[int, str]:
    text_file = open(path, encoding="utf-8")
    enum_quates = enumerate(map(str.rstrip, text_file.readlines()), start=1)
    text_file.close()
    return dict(enum_quates)
