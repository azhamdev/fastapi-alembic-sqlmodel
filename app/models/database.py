import uuid
from sqlmodel import SQLModel, Field

class Recipe(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(default="Method")
    ratio: str = Field(default="1:15")
    grind_size: str = Field(default="Medium")
    water_temp: float = Field(default=90.0)
    bean_name: str | None = None
    bean_process: str | None = None
    bean_roast_level: str | None = None
    bean_roast_date: str | None = None


class Roastery(SQLModel, table=True):
    id: uuid.UUID = Field(primary_key=True, default_factory=uuid.uuid4)
    name: str = Field(default="Unnamed Roastery")
    location: str | None = None
    established_year: str | None = None
