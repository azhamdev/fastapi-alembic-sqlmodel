from fastapi import APIRouter, Depends

from app.utils.query_params import standard_params

recipe_router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)

@recipe_router.get("/")
def get_recipes(params=Depends(dependency=standard_params)):
    return {"message": "List of recipes", "params": params, "data": [
        {"name": "Method 1", "ratio": "1:16", "grind_size": "Medium", "water_temp": 92.0, "bean_name": "Ethiopian", "bean_process": "Washed", "bean_roast_level": "Light", "bean_roast_date": "2024-01-01"},
    ]}