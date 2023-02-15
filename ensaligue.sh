#!/bin/bash

# Lecture des arguments de ligne de commande
POSTGRES_USER=${2:-postgres}
POSTGRES_PASSWORD=${3:-postgres}

# Lancement des conteneurs avec les variables d'environnement spécifiées en ligne de commande
POSTGRES_USER=$POSTGRES_USER POSTGRES_PASSWORD=$POSTGRES_PASSWORD 

#!/bin/bash

if [ "$1" = "build" ]; then
    # Lancer la commande docker-compose build
    docker compose build
elif [ "$1" = "up" ]; then
    # Lancer la commande docker-compose up -d
    docker compose up -d
elif [ "$1" = "stop" ]; then
    # Lancer la commande docker-compose stop
    docker compose stop
elif [ "$1" = "down" ]; then
    # Lancer la commande docker-compose down
    docker compose down
else
    # Afficher un message d'erreur si l'argument n'est pas valide
    echo "Wrong command: $3"
    echo "  build       Build or rebuild services"
    echo "  up          Create and start containers"
    echo "  stop        Stop containers"
    echo "  down        Stop and remove containers, networks, images, and volumes"
fi


