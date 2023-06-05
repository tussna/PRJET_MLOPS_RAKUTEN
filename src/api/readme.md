# 1. Description du dossier app
L'objectif de ce dossier est de créer une API, à l'aide du framwork FastAPI, qui permetera d'interroger les modèles créés lors de la phase de machine learnig. Après avoir crée le code de l'API, backend et frontend, nous avons crée un Dockerfile afin de pouvoir lancer l'API dans un conteneur. D'abord il faut créer le fichier requirements.txt contenant les librairies nécessair pour le contaeneur à l'aide de la commande :
- $ pip freeze > requirements.txt 

# 2. Instructions pour build
Une fois on est dans le dossier app on crée l'image de notre conteneur à l'aide de la commande :
- $ docker image build . -t rakuten-img

# 3. Instruction pour lancer le conteneur
Pour lancer le conteneur, sur le port 8000, il faut exécuter la commande :
- $ docker run -d -p 8000:8000 --name rakuten-container rakuten-img

# 4. Instruction d'arrêt
Vous pouvez arrêter l'application et libérer des ressources système en exécutant les commandes :

- $ docker container stop <container-id>
- $ docker system prune