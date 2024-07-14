# Assuming you renamed pathlib.py to example_pathlib.py

from pathlib import Path

# p = Path("copy.py")
# print(p.cwd())

def parce_file(path):
    for el in path.iterdir():
        if el.is_dir():
            parce_file(el)
        else:
            print(f"This is file: {el}")

p = Path(".")
parce_file(p)

        