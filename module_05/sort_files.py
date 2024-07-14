import shutil

from pathlib import Path

source = Path("pic/")
output = Path("backup/")

def copy_file(file: Path):
    ext = file.suffix.lstrip(".")
    new_path = output / ext
    new_path.mkdir(exist_ok=True, parents=True)
    shutil.copyfile(file, new_path / file.name)

def read_folder(path):
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else: 
            copy_file(el)

read_folder(Path(source))
