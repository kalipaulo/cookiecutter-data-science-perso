"""Utilitaires de chemins partagés si le projet en a besoin."""
from pathlib import Path


def ensure_directory(path: Path) -> Path:
    """Crée un dossier s'il n'existe pas, puis renvoie son chemin."""
    path.mkdir(parents=True, exist_ok=True)
    return path
