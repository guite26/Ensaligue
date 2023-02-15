
# ENSALIGUE

# Description

It is an application that provides an API to manage a football system. The API allows to manage players, teams, leagues and contracts.




## Authors

- [@fwallyn1](https://www.github.com/fwallyn1)
- [@gpain1999](https://www.github.com/gpain1999)





## Business constraint

For the sake of realism, here are the business constraints we have implemented.

- The contract must respect the financial constraints of a league. It is not possible to pay a player less than the minimum wage when creating a contract 

- Age must be valid when signing a contract. For example a player over 19 or under 16 cannot sign a trainee contract. Also a player under 16 cannot sign a pro contract.

- In addition, a player who already has a current contract cannot sign a new contract with dates that overlap with the current contract

- When a contract is created, an end date is not entered but a duration. In fact, the end of a contract is always on 30 June. If a player signs for 4 years then the contract will end in the 4th next 30 June

- When signing an internship contract, the duration and salary is not required. These are automatically calculated. The end date will be 30 June of the 19th year of the player's life. The salary is calculated according to a grid which is defined in the league attributes.
## API

This is what the API does :

Player Endpoints

    POST /player: create a new player by passing the Player model in the request body. Returns the created player with the id property set.
    example : {

    }
    GET /player/{id}: get a player by their id. Returns the player object.
    GET /player/: get a list of all players. Returns a list of player objects.
    DELETE /player/{id}: delete a player by their id. Returns a message confirming the deletion.
    PUT /player/{id}: update a player by their id, passing the updated Player model in the request body. Returns the updated player.

Team Endpoints

    POST /team: create a new team by passing the TeamModel model in the request body. Returns the created team with the id property set.
    GET /team/: get a list of all teams. Returns a list of team objects.
    GET /team/{id}: get a team by their id. Returns the team object.
    GET /team/{id}/contracts: get all contracts for a team by their id. Returns a list of contract objects.
    DELETE /team/{id}: delete a team by their id. Returns a message confirming the deletion.
    PUT /team/{id}: update a team by their id, passing the updated TeamModel model in the request body. Returns the updated team.
    PUT /team/{id}/promotion: promote a team to a higher league by their id. Returns the updated team.All current contracts of the team are analysed to see if they comply with the new salary rules of the new home league. If not, the salary is automatically recalculated.
    PUT /team/{id}/relegation: relegate a team to a lower league by their id. Returns the updated team. All current contracts of the team are analysed to see if they comply with the new salary rules of the new home league. If not, the salary is automatically recalculated.

League Endpoints

    POST /league: create a new league by passing the LeagueModel model in the request body. Returns the created league with the id property set.
    GET /league/: get a list of all leagues. Returns a list of league objects.
    GET /league/{id}: get a league by its id. Returns the league object.
    GET /league/{id_league}/teams: get all teams for a league by its id. Returns a list of team objects.
    GET /league/{id_league}/contracts: get all contracts for a league by its id. Returns a list of contract objects.
    PUT /league/{id}: update a league by its id, passing the updated LeagueModel model in the request body. Returns the updated league. All current league contracts are analyzed to see if they comply with the new league wage regulations. If this is not the case then the salary is automatically recalculated. 

Contract Endpoints

    POST /contract: create a new contract by passing the ContractModel model in the request body. Returns the created contract with the id property set.
    GET /contract/{id}: get a contract by its id. Returns the contract object.
    PUT /contract/{id}: update a contract by its id, passing the updated ContractModel model in the request body. Returns the updated contract.
    DELETE /contract/{id}: delete a contract by its id. Returns a message confirming the deletion.

## Running the Ensaligue Web Server and Database with Docker Compose

The Ensaligue web server and database can be easily launched using Docker Compose, along with a bash script that takes the necessary PostgreSQL username and password as arguments. This guide will explain how to launch the Ensaligue web server and database using Docker Compose and the `ensaligue.sh` script.

### Prerequisites

Before proceeding, make sure you have the following installed on your system:

- Docker Compose
- Bash

### Steps

1. Clone the Ensaligue repository to your local machine
2. Change into the `ensaligue` directory : `cd ensaligue`
3. Make the `ensaligue.sh` script executable : `chmod +x ensaligue.sh`
4. Launch the web server and database using the `ensaligue.sh` script, along with the necessary PostgreSQL username and password as arguments, and a command specified from one of "build", "up", "stop", or "down". For example, to build the images and start the containers, use the following command: `./ensaligue.sh build POSTGRES_USERNAME POSTGRES_PASSWORD `

Replace `POSTGRES_USERNAME` and `POSTGRES_PASSWORD` with the actual values for your PostgreSQL username and password.

Alternatively, you can use one of the other available commands: "up" to create and start containers, "stop" to stop containers, or "down" to stop and remove containers, networks, images, and volumes.

The Ensaligue web server and database should now be up and running in Docker Compose. You can access the web server at `http://127.0.0.1:8000`.

The API documentation can be found at `http://127.0.0.1:8000/docs#`

## Design Pattern
The strategy design pattern has been used to adapt salary and contract end date calculations based on different types of contracts (internship or professional). This approach improves modularity, maintainability, flexibility, and testability, making it easier to modify or add new calculations in the future, add new types of contracts, and write unit tests for each strategy.

## Improvements

We could have added an "active" argument for teams and leagues. When a league becomes inactive then all teams lose their arpatenances to a league and must either become inactive or change leagues.

If a team becomes inactive then all current contracts are stopped at the current date. 

Currently deleting Team and League creates membership errors in the database (league id 3 is no longer in the database while a team can still have id_league = 3 in the database)


## Database

Explanation of database creation:

    Creation of a declarative class instance (Base) that will be used to define the data models.

    Definition of the SqlAlchemy ORM data models : the player, team, league and contract tables.

    The player table contains the information on the football players (name, first name, date of birth and position).

    The team table contains information about the football teams (name and league ID).

    The league table contains information about the football leagues (name, country, level, minimum professional salary and daily salaries for the first three years of career).

    The contract table contains information on player contracts (player ID, team ID, contract start and end date, total salary and contract type).

    The columns of each table are defined using the Column class.

    The primary and foreign keys are defined using the ForeignKey class.

    The values of each column must be non-null (nullable=False).

    The as_dict methods are defined for each data model, they return a dictionary that represents the object.

The architecture of the database is as follows:

The database contains four tables: player, team, league and contract. The player table has a primary key id_player and columns name, surname, birth_date and position. The team table has a primary key id_team and columns name and id_league (foreign key of the league table). The league table has primary key id_league and columns name, country, level, professional_minimum_wage, daily_salary_first_year, daily_salary_second_year and daily_salary_third_year. The contract table has a primary key id_contract and columns id_player (foreign key of the player table), id_team (foreign key of the team table), date_start, date_end, total_salary and type_contract.


