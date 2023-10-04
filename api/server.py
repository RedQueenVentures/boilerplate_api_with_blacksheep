from blacksheep import Application, FromJSON, Response
from blacksheep.exceptions import BadRequest, NotFound
from blacksheep.server.openapi.v3 import OpenAPIHandler
from blacksheep.server.responses import pretty_json
from api.constants import (not_created_message, not_found_message, not_found_by_id_message)
from datetime import datetime
from api.db.tables.cat import Cat
from api.db.tables.person import Person
from dotenv import load_dotenv
from api.models.person import (PersonModelRequest)
from api.models.cat import (CatModelRequest)
from openapidocs.v3 import Info
import os
from piccolo.engine import engine_finder
import uuid

load_dotenv()

ENVIRONMENT = os.environ.get("ENVIRONMENT", "local")
# 👇 For security reasons, we only want this variable to be true in a local environment
SHOW_ERROR_DETAILS = os.environ.get("SHOW_ERROR_DETAILS", None)

if ENVIRONMENT in ["local"]:
    os.environ[SHOW_ERROR_DETAILS] = "true"
    app = Application(show_error_details=SHOW_ERROR_DETAILS)
else:
    os.environ[SHOW_ERROR_DETAILS] = "false"
    app = Application(show_error_details=SHOW_ERROR_DETAILS)

delete = app.router.delete
get = app.router.get
post = app.router.post
put = app.router.put

docs = OpenAPIHandler(info=Info(title="Boilerplate Python API with BlackSheep Framework", version="0.0.1"))
docs.bind_app(app)

# -------------------------------------------------------------------------------------------

@get("/")
def home():
    return f"\nHello, World! {datetime.utcnow().isoformat()}"

@get("/crash_test")
def crash_test():
    raise Exception("Crash test")

# -------------------------------------------------------------------------------------------

@get("/persons")
async def persons() -> Response:
    """
    Gets a list of all Persons
    """
    try:
        print(f"\nGetting a list of all Persons...")
        persons = await Person.select()
        return pretty_json(data=persons, status=200)
    except Exception as e:
        raise NotFound(message=not_found_message(ent='Persons', ex=e))


@get("/persons/{id}")
async def persons(id: str) -> Response:
    """
    Gets a Person by its id
    """
    try:
        print(f"\nGetting Person by id {id}...")
        person = await Person.select().where(id==Person.id).first()
        return pretty_json(data=person, status=200)
    except Exception as e:
        raise NotFound(message=not_found_by_id_message(ent='Person', id=id, ex=e))


@post("/persons")
async def persons(req: FromJSON[PersonModelRequest]) -> Response:
    """
    Creates a new Person
    """
    try:
        print("\nCreating new Person...")
        person = Person(**req.value.dict())

        if person.id is None:
            person.id = uuid.uuid4()

        if person.datetime_created is None:
            person.datetime_created = datetime.utcnow()
            # Set modified to the same value as created
            person.datetime_modified = person.datetime_created

        await person.save().run()
        created_person = await Person.select().where(person.id==Person.id).first()
        return pretty_json(data=created_person, status=201)
    except Exception as e:
        raise BadRequest(message=not_created_message(ent='Person', ex=e))

# -------------------------------------------------------------------------------------------

@get("/cats")
async def cats() -> Response:
    """
    Gets a list of all Cats
    """
    try:
        print(f"\nGetting a list of all Cats...")
        cats = await Cat.select()
        return pretty_json(data=cats, status=200)
    except Exception as e:
        raise NotFound(message=not_found_message(ent='Cats', ex=e))


@get("/cats/{id}")
async def cats(id: str) -> Response:
    """
    Gets a Cat by its id
    """
    try:
        print(f"\nGetting Cat by id {id}...")
        cat = await Cat.select().where(id==Cat.id)
        return pretty_json(data=cat, status=200)
    except Exception as e:
        raise NotFound(message=not_found_by_id_message(ent='Cat', id=id, ex=e))


@post("/cats")
async def cats(req: FromJSON[CatModelRequest]) -> Response:
    """
    Creates a new Cat
    """
    try:
        print("\nCreating new Cat...")

        cat = Cat(**req.value.dict())
        if cat.id is None:
            cat.id = uuid.uuid4()

        await cat.save().run()
        created_cat = await Cat.select().where(cat.id==Cat.id).first()
        
        return pretty_json(data=created_cat, status=201)
    except Exception as e:
        raise BadRequest(message=not_created_message(ent='Cat', ex=e))

# -------------------------------------------------------------------------------------------

# TODO: Either move db session code to another file or move routes (above) to a separate file
async def open_database_connection_pool(application):
    print("Opening database connection pool...")
    try:
        # TODO: Tables need to be created (if they don't exist) prior to executing transactions; handle this here?
        engine = engine_finder()
        await engine.start_connection_pool()
        await Cat.create_table(if_not_exists=True)
        await Person.create_table(if_not_exists=True)
    except Exception as e:
        print(f"Unable to connect to the database. Details: \n{e}")


async def close_database_connection_pool(application):
    print("\nClosing database connection pool...")
    try:
        engine = engine_finder()
        await engine.close_connection_pool()
    except Exception as e:
        print(f"Unable to close connection to the database. Details: \n{e}")


app.on_start += open_database_connection_pool
app.on_stop += close_database_connection_pool
