from fastapi import FastAPI, status, APIRouter
from database.database import Base, engine, PlayerDB
from pydantic import BaseModel
from sqlalchemy.orm import Session
from business_objects.player import Player

router = APIRouter()

# Create the database
Base.metadata.create_all(engine)

# Initialize app
app = FastAPI()

# <irrelevant code here..>
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/player", status_code=status.HTTP_201_CREATED,tags=['player'])
def add_player(player: Player):

    # create a new database session
    session = Session(bind=engine, expire_on_commit=False)

    # create an instance of the ToDo database model
    playerdb = PlayerDB(name = player.name,surname=player.surname,birth_date=player.birth_date,position=player.position)

    # add it to the session and commit it
    session.add(playerdb)
    session.commit()

    # grab the id given to the object from the database
    id = playerdb.id_player

    # close the session
    session.close()

    # return the id
    return f"created todo item with id {id}"

# <irrelevant code here..>
