from pydantic import BaseModel

class RecipeRequest(BaseModel):
    name: str
    ratio: str
    grind_size: str | None = None
    water_temp: float
    bean_name: str | None = None
    bean_process: str | None = None
    bean_roast_level: str | None = None
    bean_roast_date: str | None = None

class RecipeResponse(BaseModel):
    id: str
    name: str
    ratio: str
    grind_size: str | None = None
    water_temp: float
    bean_name: str | None = None
    bean_process: str | None = None
    bean_roast_level: str | None = None
    bean_roast_date: str | None = None
