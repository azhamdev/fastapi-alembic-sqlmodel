from pydantic import BaseModel

class RoasteryRequest(BaseModel):
    name: str
    location: str | None = None
    established_year: int | None = None

class RoasteryResponse(BaseModel):
    id: str
    name: str
    location: str | None = None
    established_year: int | None = None