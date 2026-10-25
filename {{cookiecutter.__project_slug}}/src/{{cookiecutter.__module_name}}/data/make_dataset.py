"""Fonctions de départ pour charger et préparer les données."""
from pathlib import Path
import pandas as pd

from {{ cookiecutter.__module_name }}.config import RAW_DATA_DIR, INTERIM_DATA_DIR


def load_raw_csv(filename: str, **read_csv_kwargs) -> pd.DataFrame:
    """Charge un CSV depuis data/raw/ sans modifier le fichier source."""
    path = RAW_DATA_DIR / filename
    if not path.is_file():
        raise FileNotFoundError(f"Fichier introuvable : {path}")
    return pd.read_csv(path, **read_csv_kwargs)


def save_interim_csv(df: pd.DataFrame, filename: str, index: bool = False) -> Path:
    """Enregistre un résultat intermédiaire dans data/interim/."""
    INTERIM_DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = INTERIM_DATA_DIR / filename
    df.to_csv(path, index=index)
    return path
