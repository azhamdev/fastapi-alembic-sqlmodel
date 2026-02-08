from fastapi import APIRouter, Depends

from app.utils.query_params import standard_params

roastery_router = APIRouter(
    prefix="/roasteries",
    tags=["roasteries"],
)

@roastery_router.get("/")
def get_roasteries(params=Depends(dependency=standard_params)):
    return {"message": "List of roasteries", "params": params, "data": [
        {"name": "Tradisine", "location": "Slawi", "established_year": 2010},
    ]}