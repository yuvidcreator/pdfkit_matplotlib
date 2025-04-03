from functools import lru_cache



def get_string_methods():
    i: int = 0
    for method in dir(int):
        if '__' not in method:
            i += 1
            print(i, method, sep=': ')


get_string_methods()