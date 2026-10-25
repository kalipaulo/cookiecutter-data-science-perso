# Modèle personnel Cookiecutter — Data Science

Ce dépôt est un **modèle de projet**, pas un projet d'analyse lui-même. Il sert à générer une nouvelle arborescence Data Science homogène à chaque projet.

## 1. Ce que contient le modèle

- `cookiecutter.json` : les questions et valeurs par défaut proposées lors de la génération.
- `{{cookiecutter.project_slug}}/` : tous les fichiers et dossiers qui seront copiés dans le nouveau projet.
- `STRUCTURE_FR.md` dans le projet généré : explication en français de chaque dossier et des règles de rangement.

## 2. Installer Cookiecutter

Dans un terminal PowerShell, installe l'outil dans l'environnement Python que tu réserves aux outils de génération :

```powershell
python -m pip install --upgrade cookiecutter
```

Cookiecutter peut rester installé dans ton environnement habituel. Il n'est pas nécessaire de le réinstaller dans chaque environnement de projet.

## 3. Générer un nouveau projet depuis ce modèle local

Place-toi dans le dossier où tu veux créer le nouveau projet. Remplace le chemin ci-dessous par le chemin où tu as conservé ce dossier de modèle :

```powershell
cd "C:/Users/TON_UTILISATEUR/Documents/Modeles"
cookiecutter "C:/Users/TON_UTILISATEUR/Documents/Modeles/cookiecutter_data_science_perso"
```

Cookiecutter te posera les questions de `cookiecutter.json`. Appuie sur Entrée pour accepter la valeur entre parenthèses, ou saisis une nouvelle valeur.

Un dossier portant le nom `project_slug` sera créé dans le dossier courant. Il contiendra la structure complète du projet.

> Important : conserve le dossier `cookiecutter_data_science_perso` à un emplacement stable. Pour chaque nouveau projet, exécute la commande depuis le dossier parent où tu veux le créer. Ne lance pas la génération à l'intérieur d'un projet existant.

## 4. Premier démarrage du projet généré

Depuis le dossier nouvellement créé :

```powershell
conda env create -f environment.yml
conda activate NOM_DU_MODULE
python -m pip install -e .
python -m pytest tests -v
```

`NOM_DU_MODULE` correspond à la valeur donnée à `module_name` au moment de la génération. Si tu ne souhaites pas utiliser Conda, crée un environnement virtuel Python et installe les dépendances listées dans `environment.yml` avec une méthode adaptée.

## 5. Utiliser le template officiel Cookiecutter Data Science

Le modèle officiel est une bonne base de départ et la commande `ccds` génère le template officiel v2. Pour ton **modèle personnalisé**, utilise plutôt la commande `cookiecutter` avec le chemin de ce dossier. Cela permet de conserver tes propres noms, dossiers et documentation d'un projet à l'autre.

Documentation officielle :
- Cookiecutter Data Science : https://cookiecutter-data-science.drivendata.org/
- Utilisation du template : https://cookiecutter-data-science.drivendata.org/using-the-template/
- Cookiecutter générique : https://cookiecutter.readthedocs.io/en/stable/overview.html
