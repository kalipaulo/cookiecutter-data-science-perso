"""Point d'entrée pour les transformations de variables réutilisables."""
import pandas as pd


def build_features(df: pd.DataFrame) -> pd.DataFrame:
    """Construit les variables explicatives.

    Remplacer le comportement de départ par des transformations explicites,
    testées et reproductibles. La fonction renvoie ici une copie sans modifier
    le tableau transmis par l'appelant.
    """
    return df.copy()
