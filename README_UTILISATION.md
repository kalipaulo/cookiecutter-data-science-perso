# Utiliser le modèle Cookiecutter Data Science Kalipolo

## 🇫🇷 Français

Ce dépôt est un **modèle de projet**. Il ne contient pas l'analyse d'un jeu de données spécifique : Cookiecutter s'en sert pour générer un nouveau projet avec une structure cohérente.

### Générer depuis GitHub

Installe Python et Git, puis installe Cookiecutter :

```powershell
python -m pip install --upgrade cookiecutter
```

Depuis le dossier dans lequel tu veux créer le projet, lance :

```powershell
cookiecutter gh:kalipaulo/cookiecutter-data-science-perso
```

Cookiecutter pose quatre questions :

1. **Nom du projet** : nom lisible qui apparaîtra dans le README et les titres.
2. **Nom de l'auteur** : nom de la personne ou de l'équipe à afficher.
3. **Description courte** : objectif du projet en une phrase.
4. **Version de Python cible** : tape le numéro correspondant à la version souhaitée. Le choix est inscrit dans `environment.yml` et `pyproject.toml`. Appuie sur Entrée pour garder la première option proposée.

Le nom du dossier (`analyse-des-ventes`) et le nom du package Python (`analyse_des_ventes`) sont calculés automatiquement depuis le nom du projet. Tu ne dois pas les saisir séparément.

### Démarrer le projet généré

Depuis le dossier créé par Cookiecutter :

```powershell
conda env create -f environment.yml
conda activate NOM-DU-PROJET
python -m pip install -e .
python -m pytest tests -v
```

Remplace `NOM-DU-PROJET` par le nom du dossier généré, affiché lors de la création. Tu peux aussi utiliser `python -m venv .venv` si tu ne souhaites pas utiliser Conda.

## 🇬🇧 English

This repository is a **project template**, not a project containing a specific data analysis. Cookiecutter uses it to generate a new project with a consistent structure.

Install Cookiecutter, then run this command from the parent directory where the new project should be created:

```powershell
python -m pip install --upgrade cookiecutter
cookiecutter gh:kalipaulo/cookiecutter-data-science-perso
```

You will be asked for the human-readable project name, author, one-sentence description, and target Python version. The folder slug and importable Python package name are generated automatically from the project name.

See `STRUCTURE_FR.md` in the generated project for a detailed French explanation of each folder.
