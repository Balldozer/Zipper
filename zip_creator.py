import zipfile
import pathlib


def make_archives(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as file:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            file.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archives(["Bonus1.py", "Bonus3.py"], "dest")
