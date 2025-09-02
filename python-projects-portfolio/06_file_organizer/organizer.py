import os, shutil, sys, pathlib

def organize(folder):
    p = pathlib.Path(folder)
    for file in p.iterdir():
        if file.is_file():
            ext = file.suffix[1:] or "no_ext"
            target = p / ext
            target.mkdir(exist_ok=True)
            shutil.move(str(file), target / file.name)

if __name__ == "__main__":
    organize(sys.argv[1] if len(sys.argv) > 1 else ".")
