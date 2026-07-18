from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile
import shutil


def ensure_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def download_file(url: str, destination: Path) -> None:

    if destination.exists():
        print(f"Already exists: {destination.name}")
        return

    print(f"Downloading: {destination.name}")

    urlretrieve(url, destination)

    print("Download complete")


def extract_zip(zip_path: Path, extract_to: Path) -> None:
    if extract_to.exists() and any(extract_to.iterdir()):
        print(f"Already extracted: {extract_to.name}")
        return

    print(f"Extracting: {zip_path.name}")

    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    print("Extraction complete")


def folder_size(folder: Path) -> float:

    total = 0

    for file in folder.rglob("*"):
        if file.is_file():
            total += file.stat().st_size

    return total / (1024 ** 3)