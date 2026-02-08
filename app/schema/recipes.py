from pydantic import BaseModel

class RecipeRequest(BaseModel):
    name: str
    ratio: str
    grind_size: str | None = None
    water_temp: float

class RecipeResponse(BaseModel):
    id: str
    name: str
    ratio: str
    grind_size: str | None = None
    water_temp: float
