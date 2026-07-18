from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

print("=" * 60)
print("PROJECT PATH TEST")
print("=" * 60)

print("Project Root:")
print(PROJECT_ROOT)

print()

print("ML Folder Exists:")
print((PROJECT_ROOT / "ml").exists())

print()

print("App Folder Exists:")
print((PROJECT_ROOT / "app").exists())

print()

print("Docs Folder Exists:")
print((PROJECT_ROOT / "docs").exists())

print("=" * 60)