from .common.file_operations import save_to_file
def find_in(iterable,finder,expected):
    for i in iterable:
        if finder(i)==expected:
            return  i
    raise NotFoundError(f"{expected} not found provited iterable")

class NotFoundError(Exception):
    pass

print(__name__)

print("probando El archivo find.py")
