from app.models.engine import get_db
from app.models.database import Roastery
from app.schema.roasteries import RoasteryRequest
from sqlmodel import select
from fastapi import APIRouter, Depends, status
from app.utils.query_params import standard_params

roastery_router = APIRouter(
    prefix="/roasteries",
    tags=["roasteries"],
)

@roastery_router.get("/", status_code=status.HTTP_200_OK)
def get_roasteries(params=Depends(dependency=standard_params), db=Depends(dependency=get_db)):
    stmt = select(Roastery)
    result = db.exec(stmt)
    roasteries = result.all()

    return {"total": len(roasteries), "data": roasteries}

@roastery_router.post("/")
def create_roastery(body: RoasteryRequest, db=Depends(dependency=get_db)):
    new_roastery = Roastery(
        name=body.name,
        location=body.location,
        established_year=body.established_year,
    )
    db.add(new_roastery)
    db.commit()
    db.refresh(new_roastery)

    return {"message": "Roastery created successfully", "roastery": new_roastery}
