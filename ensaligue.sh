#!/bin/bash

# Lecture des arguments de ligne de commande
POSTGRES_USER=${1:-postgres}
POSTGRES_PASSWORD=${2:-postgres}

# Lancement des conteneurs avec les variables d'environnement spécifiées en ligne de commande
POSTGRES_USER=$POSTGRES_USER POSTGRES_PASSWORD=$POSTGRES_PASSWORD docker-compose up -d

