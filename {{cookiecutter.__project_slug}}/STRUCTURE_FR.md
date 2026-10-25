# Guide de la structure du projet — en français

Ce projet suit une organisation inspirée de Cookiecutter Data Science. La structure est un cadre réutilisable : tous les dossiers ne doivent pas être remplis dès le premier jour.

## Arborescence

```text
{{ cookiecutter.__project_slug }}/
├── config/                     # Paramètres modifiables du projet
├── data/
│   ├── raw/                    # Données originales, non modifiées
│   ├── external/               # Données provenant de sources externes
│   ├── interim/                # Données transformées temporairement
│   └── processed/              # Données préparées pour analyse/modélisation
├── docs/
│   └── decisions/              # Décisions d'architecture ou de méthode
├── models/                     # Artefacts des modèles entraînés
├── notebooks/                  # Exploration et expérimentations
├── outputs/
│   └── predictions/            # Prédictions et livrables tabulaires finaux
├── references/                 # Dictionnaires, manuels et sources documentaires
├── reports/
│   ├── figures/                # Graphiques exportés
│   └── tables/                 # Tableaux exportés pour les rapports
├── src/{{ cookiecutter.__module_name }}/
│   ├── config.py               # Chemins et configuration centrale
│   ├── data/                   # Chargement, validation et préparation des données
│   ├── features/               # Création et transformation des variables
│   ├── models/                 # Entraînement, évaluation et prédiction
│   ├── visualization/          # Fonctions de visualisation réutilisables
│   └── utils/                  # Utilitaires communs et indépendants du métier
├── tests/                      # Tests automatisés du code
├── environment.yml             # Dépendances Conda
├── pyproject.toml              # Métadonnées, installation et configuration Python
├── Makefile                    # Raccourcis de commandes courantes
├── .gitignore                  # Fichiers/dossiers exclus de Git
└── README.md                   # Présentation et guide de démarrage
```

## Rôle de chaque dossier

| Dossier | À quoi sert-il ? | Exemples de contenu |
|---|---|---|
| `config/` | Stocker les paramètres modifiables sans changer la logique du code. | `base.yaml`, seuils, graine aléatoire, paramètres de modèles. Ne pas y stocker de mots de passe. |
| `data/raw/` | Conserver la version d'origine des données. Ne jamais la modifier manuellement ou l'écraser. | CSV reçus, exports d'origine. |
| `data/external/` | Conserver des sources supplémentaires provenant d'organismes, d'API ou de fournisseurs. | Données publiques externes, référentiels. |
| `data/interim/` | Sauvegarder des étapes intermédiaires utiles, si elles doivent être réutilisées. | Données harmonisées, jointures provisoires. |
| `data/processed/` | Conserver des données préparées selon des règles explicites. | Table analytique finale ou jeu de features prêt à l'emploi. |
| `docs/` | Expliquer la méthode, l'architecture et les décisions propres au projet. | `methodology.md`, `model_card.md`, historique de décisions. |
| `docs/decisions/` | Garder une trace des décisions importantes et de leurs justifications. | Pourquoi un modèle ou une métrique a été retenu. |
| `models/` | Enregistrer les modèles ajustés et leurs artefacts. | Pipeline `.joblib`, modèle LightGBM, métadonnées de modèle. |
| `notebooks/` | Explorer, visualiser, tester des idées et documenter une analyse. | Notebooks numérotés `01_data_audit.ipynb`, `02_eda.ipynb`. |
| `outputs/` | Rassembler les livrables finaux destinés à être exportés ou remis. | Prédictions, scores, fichiers d'échange. |
| `outputs/predictions/` | Séparer les prédictions du reste des livrables. | `predictions.csv`, `submission.csv` lorsqu'une compétition l'exige. |
| `references/` | Garder les documents source nécessaires pour comprendre les données. | Dictionnaire des variables, documentation technique, règles d'une compétition. |
| `reports/` | Regrouper les rapports et les éléments graphiques qui les accompagnent. | Rapport final, synthèse d'analyse. |
| `reports/figures/` | Stocker les figures exportées par le code ou les notebooks. | Courbes ROC, distributions, importance des variables. |
| `reports/tables/` | Stocker les tableaux exportés pour les rapports. | Comparaison de modèles, statistiques descriptives. |
| `src/<module>/data/` | Écrire les fonctions réutilisables qui chargent, vérifient et préparent les données. | `make_dataset.py`, validation de schéma. |
| `src/<module>/features/` | Créer les variables explicatives et les transformations réutilisables. | Ratios, agrégations, transformations métier. |
| `src/<module>/models/` | Entraîner, évaluer et utiliser les modèles. | `train_model.py`, `evaluate_model.py`, `predict_model.py`. |
| `src/<module>/visualization/` | Écrire les fonctions qui génèrent les graphiques. | Fonction de courbe ROC ou de comparaison des scores. |
| `src/<module>/utils/` | Placer les utilitaires réellement partagés par plusieurs modules. | Gestion de chemins, fonctions génériques. Éviter le fourre-tout. |
| `tests/` | Vérifier automatiquement le comportement attendu du code. | Tests de fonctions, de schémas, de probabilités et de formats de sortie. |

## Rôle des fichiers principaux

- `README.md` : objectif, installation, utilisation et état du projet.
- `STRUCTURE_FR.md` : explication de l'arborescence et règles de rangement.
- `environment.yml` : dépendances Conda permettant de recréer l'environnement.
- `pyproject.toml` : métadonnées du package Python et paramètres des outils de développement.
- `Makefile` : raccourcis facultatifs. Sur Windows, il faut disposer d'un outil compatible avec `make` ; les commandes Python peuvent toujours être lancées directement.
- `.gitignore` : empêche l'ajout accidentel de données, environnements virtuels et artefacts générés dans Git.
- `src/<module>/config.py` : chemins calculés à partir du projet, sans chemin absolu lié à un ordinateur particulier.
- `LICENSE` (facultatif) : à ajouter si le code est distribué. Choisir explicitement une licence adaptée ; la licence du code ne remplace pas les conditions d’utilisation des données.

## Le parcours des données

```text
Source d'origine -> data/raw -> data/interim -> data/processed -> modèle/analyse -> outputs/ et reports/
```

C'est un parcours indicatif, pas une obligation : un projet peut sauter une étape s'il n'en a pas besoin. Les fichiers d'origine restent inchangés ; toute transformation se fait par du code versionné.

## Règles de travail

1. **Un dossier = une responsabilité principale.** Si tu ne peux pas expliquer pourquoi un fichier appartient à un dossier, revois son emplacement.
2. **Le notebook sert à explorer ; `src/` sert à conserver le code réutilisable.** Quand une cellule devient utile dans plusieurs analyses, transforme-la en fonction dans `src/`.
3. **Un test vérifie le code ; il ne mesure pas la qualité scientifique du modèle.** Évalue séparément les métriques comme ROC-AUC, F1, RMSE ou MAE selon le problème.
4. **Ne versionne pas les données par défaut.** Vérifie les licences, la confidentialité, les tailles des fichiers et les règles du fournisseur.
5. **Évite les duplications.** Si une source doit rester à un chemin spécial imposé par une compétition, garde ce chemin et documente-le au lieu de multiplier les copies.
6. **Ajoute les dossiers à la demande.** Ne crée pas un nouveau dossier sans fichier ou besoin identifiable.
7. **N'utilise jamais de chemins absolus propres à ton PC dans le code.** Calcule les chemins depuis la racine du projet ou lis-les dans la configuration.

## Comment décider où ranger un fichier ?

- Code de chargement ou de nettoyage réutilisable → `src/<module>/data/`.
- Code de création de variables → `src/<module>/features/`.
- Code d'entraînement/prediction → `src/<module>/models/`.
- Exploration provisoire → `notebooks/`.
- Test automatisé → `tests/`.
- Modèle déjà entraîné → `models/`.
- Source ou dictionnaire reçu → `references/`.
- Décision/méthode du projet → `docs/`.
- Graphique/tableau exporté → `reports/figures/` ou `reports/tables/`.
- Prédiction ou livrable final → `outputs/`.
- Paramètre modifiable → `config/`.

## Exceptions propres à une compétition

Une compétition peut imposer des chemins comme `input/` et `output/submission.csv`, ou des notebooks comme `tutorial.ipynb`. Respecte ces exigences. Le modèle générique ne doit pas déplacer ni renommer automatiquement ces fichiers ; il faut ajouter les dossiers et conventions spécifiques dans le projet concerné.
