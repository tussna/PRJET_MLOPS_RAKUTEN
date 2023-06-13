# PROJET_MLOPS_RAKUTEN

# 2. Strecture de l'application
Code de fin de projet MLOPS. Dans cette partie nous décrivons la méthodologie utilisée pour ce projet MLOps en deep/machine learning.

## 2.1 datas
La première partie concerne le dossier des données du projets composés des fichiers csv et images.

## 2.2 src
Ce dossier englope tous la source du code de l'application et se décompose en trois dossiers principales.

## 2.2.1 Machine_Deep_Learning_Models
Ce dossier est pour le but de nettoyer et encoder des données textuelles et images. Et puis d'entrainer des modèles classifications. Enfin, les modèles les plus pertinents sont sauvegardés pour être utilisés dans la partie qui suit.

## 2.2.2 app
Le dossier est pour le but la création d'une API à l'aide du framwork FastAPI où les dépendances sont stockées dans requirements.txt qui servera au conteneur de l'API via un fichier Dockerfile. Pour rendre l'API plus atractive, le dossier contient des fichiers html, css (notament bootstrap) et jss.

## 22..3 tests
Essais d'automatiser l'API avec des fichiers Docker & Docker-Compose (des fichiers docker complémentaires doivent être créés pour les tests).
