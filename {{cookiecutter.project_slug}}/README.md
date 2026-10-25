# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

**Auteur :** {{ cookiecutter.author_name }}  
**Module Python :** `{{ cookiecutter.module_name }}`

## Objectif

Décrire ici le problème métier ou scientifique, la population étudiée, la question à résoudre et les livrables attendus.

## Démarrage rapide

```bash
conda env create -f environment.yml
conda activate {{ cookiecutter.module_name }}
python -m pip install -e .
python -m pytest tests -v
```

## Organisation

Lire [`STRUCTURE_FR.md`](STRUCTURE_FR.md) avant de commencer : ce document explique où placer les données, les notebooks, le code source, les modèles et les résultats.

## Données

Les données ne sont pas fournies avec ce dépôt. Indiquer ici leur provenance, les règles d'accès et la procédure de récupération. Les données privées, réglementées ou fournies par une compétition ne doivent pas être versionnées par défaut.

## Reproduction

Documenter ici les commandes nécessaires pour reproduire l'analyse, entraîner le modèle et générer les livrables. Ne déclarer une commande reproductible qu'après l'avoir réellement testée.

## Résultats et limites

Résumer ici les principaux résultats une fois disponibles, les métriques d'évaluation, les limites connues et les précautions d'interprétation.
