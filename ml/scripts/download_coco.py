from pathlib import Path

from ml.configs.paths import COCO_DIR
from ml.scripts.download_utils import (
    ensure_directory,
    download_file,
    extract_zip,
    folder_size,
)

COCO_FILES = {
    "train2017.zip": "http://images.cocodataset.org/zips/train2017.zip",
    "val2017.zip": "http://images.cocodataset.org/zips/val2017.zip",
    "annotations_trainval2017.zip": "http://images.cocodataset.org/annotations/annotations_trainval2017.zip",
}


def main() -> None:
    ensure_directory(COCO_DIR)

    print("=" * 70)
    print("COCO DATASET DOWNLOAD")
    print("=" * 70)

    for filename, url in COCO_FILES.items():

        zip_path = COCO_DIR / filename

        extract_folder = COCO_DIR / filename.replace(".zip", "")

        download_file(url, zip_path)

        extract_zip(zip_path, extract_folder)

        print()

    print("=" * 70)
    print("DOWNLOAD SUMMARY")
    print("=" * 70)

    print(f"Dataset Folder : {COCO_DIR}")
    print(f"Current Size   : {folder_size(COCO_DIR):.2f} GB")

    print("=" * 70)


if __name__ == "__main__":
    main()