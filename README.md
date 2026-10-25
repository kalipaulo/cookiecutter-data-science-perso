# Cookiecutter Data Science Kalipolo

**Un modèle réutilisable de projet Data Science / A reusable Data Science project template.**

[Français](#français) · [English](#english)

## Français

Ce dépôt public permet de générer rapidement un projet Data Science organisé, documenté et prêt à évoluer. Il s'adresse aux débutants comme aux utilisateurs expérimentés.

### Fonctionnalités

- Structure claire pour les données, notebooks, code source, tests, rapports et livrables.
- Nom du dossier et package Python dérivés automatiquement du nom du projet.
- Choix de la version de Python, reporté dans les fichiers de configuration.
- Fichier `STRUCTURE_FR.md` dans chaque projet généré, expliquant les dossiers en français.
- Licence MIT.

### Utilisation rapide

Prérequis : Python et Git installés.

```bash
python -m pip install --upgrade cookiecutter
cookiecutter gh:kalipaulo/cookiecutter-data-science-perso
```

Cookiecutter demande le nom lisible du projet, l'auteur, une courte description et la version Python ciblée. Il crée automatiquement le dossier du projet et le nom importable du package : ne les saisissez pas séparément.

Les instructions détaillées sont dans [`README_UTILISATION.md`](README_UTILISATION.md). La structure générée est expliquée dans `STRUCTURE_FR.md`.

## English

This public repository generates a structured, documented, and extensible Data Science project. It is designed for both beginners and experienced practitioners.

### Features

- Clear separation for data, notebooks, source code, tests, reports, and outputs.
- Project folder slug and Python import package are derived from the project name.
- Choose a Python version; the selection is written to the generated configuration files.
- Every generated project includes `STRUCTURE_FR.md`, a French folder-by-folder guide.
- MIT License.

### Quick start

Requirements: Python and Git.

```bash
python -m pip install --upgrade cookiecutter
cookiecutter gh:kalipaulo/cookiecutter-data-science-perso
```

Cookiecutter asks for a human-readable project name, author, short description, and target Python version. It automatically derives the project directory and Python import package names.

See [`README_UTILISATION.md`](README_UTILISATION.md) for detailed instructions.

## License

This template is released under the MIT License. See [`LICENSE`](LICENSE).
