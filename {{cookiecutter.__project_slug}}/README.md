# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

**Auteur / Author:** {{ cookiecutter.author_name }}  
**Dossier du projet / Project folder:** `{{ cookiecutter.__project_slug }}`  
**Package Python / Python import package:** `{{ cookiecutter.__module_name }}`  
**Version de Python / Python version:** `{{ cookiecutter.python_version }}`

## Objectif / Purpose

Décrire ici le problème métier ou scientifique, la population étudiée, la question à résoudre et les livrables attendus.

Describe the problem, target population, research question, and expected deliverables here.

## Démarrage rapide / Quick start

### Avec Conda / With Conda

```bash
conda env create -f environment.yml
conda activate {{ cookiecutter.__project_slug }}
python -m pip install -e .
python -m pytest tests -v
```

### Avec un environnement virtuel Python / With a Python virtual environment

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
python -m pytest tests -v
```

## Organisation / Project structure

Lire [`STRUCTURE_FR.md`](STRUCTURE_FR.md) pour connaître le rôle de chaque dossier. / Read [`STRUCTURE_FR.md`](STRUCTURE_FR.md) for the folder-by-folder explanation (French).

## Données / Data

Les données ne sont pas incluses dans ce modèle. Documenter leur provenance, les règles d'accès et la procédure de récupération. Ne versionnez pas les données privées ou soumises à des restrictions. / Data are not included in this template. Document their source and access rules; do not commit private or restricted data.

## Reproduction / Reproducibility

Documenter les commandes permettant de reproduire les analyses, entraîner les modèles et générer les livrables. Ne déclarer une procédure reproductible qu'après l'avoir testée. / Document the commands required to reproduce analyses, train models, and produce deliverables. Only claim reproducibility after testing it.
