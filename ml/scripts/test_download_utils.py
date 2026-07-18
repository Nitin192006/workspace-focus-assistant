from pathlib import Path

from ml.scripts.download_utils import ensure_directory

test_dir = Path("ml/test_directory")

ensure_directory(test_dir)

print("=" * 50)

print("Directory Exists:", test_dir.exists())

print("Directory:", test_dir)

print("=" * 50)