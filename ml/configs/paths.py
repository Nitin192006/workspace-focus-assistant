from pathlib import Path

# Root of the repository
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ML directory
ML_ROOT = PROJECT_ROOT / "ml"

# Dataset directories
DATASETS_DIR = ML_ROOT / "datasets"
COCO_DIR = DATASETS_DIR / "coco"
FILTERED_DATASET_DIR = DATASETS_DIR / "workspace_focus"

# Model directories
MODELS_DIR = ML_ROOT / "models"
CHECKPOINTS_DIR = MODELS_DIR / "checkpoints"
EXPORTS_DIR = ML_ROOT / "exports"

# Evaluation
EVALUATION_DIR = ML_ROOT / "evaluation"

# Notebooks
NOTEBOOKS_DIR = ML_ROOT / "notebooks"

# Create directories if missing
for directory in [
    DATASETS_DIR,
    COCO_DIR,
    FILTERED_DATASET_DIR,
    CHECKPOINTS_DIR,
    EXPORTS_DIR,
]:
    directory.mkdir(parents=True, exist_ok=True)