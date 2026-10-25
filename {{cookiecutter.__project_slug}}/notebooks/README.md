# Notebooks

Convention de nommage recommandée : `01_data_audit.ipynb`, `02_eda.ipynb`, `03_modeling.ipynb`.

- `01_data_audit` : contrôle de structure et de qualité.
- `02_eda` : exploration descriptive et visualisations.
- `03_modeling` : baseline, validation et comparaison de modèles.

Les notebooks servent à explorer. Le code stable appelé depuis plusieurs endroits doit être déplacé dans `src/{{ cookiecutter.module_name }}/`.
