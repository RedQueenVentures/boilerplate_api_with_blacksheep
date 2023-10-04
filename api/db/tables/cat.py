from piccolo.columns import Column, UUID, Varchar
from piccolo.table import Table

# Timestamps are prefaced with `datetime_` to visually and alphabetically 'chunk'
# them together for easier reference 

class Cat(Table, help_text="A 'Cat' entity"):
    """
    A 'Cat' entity
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_json(self):
        return {
            'breed': self.breed,
            'id': self.id,
            'gender': self.gender,
            'name': self.name,
        }


    breed: Column = Varchar(
        null=True,
        required=True
    )
    gender: Column = Varchar(
        null=True,
        required=True
    )
    id: Column = UUID(
        primary_key=True,
        null=False,
        required=False,
        unique=True
    )
    name: Column = Varchar(
        null=True,
        required=True
    )
