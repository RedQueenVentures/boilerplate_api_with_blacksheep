from api.db.tables.person import Person
from piccolo.utils.pydantic import create_pydantic_model
from typing import Any

# ModelNamePartial 👉 the model a function received as an argument when we want to modify data in the db, for example, when using a PATCH method
# ModelNameResponse 👉 the model that a function returns when using any endpoint and includes default columns like `id`
# ModelNameRequest 👉 the model or structure we use when we add new data to the database (using POST); If we try to enter data without the fields we specified in our table, it will return an error

PersonModelPartial: Any = create_pydantic_model(
    all_optional=True,
    include_default_columns=False,
    model_name="PersonModelResponse",
    table=Person,
)

PersonModelRequest: Any = create_pydantic_model(
    all_optional=True,
    include_default_columns=False,
    model_name="PersonModelRequest",
    table=Person,
)

PersonModelResponse: Any = create_pydantic_model(
    include_default_columns=True,
    model_name="PersonModelResponse",
    table=Person,
)
