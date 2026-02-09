from app.schema.recipes import RecipeRequest, RecipeResponse
from fastapi import APIRouter, Depends, status

from app.utils.query_params import standard_params

recipe_router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)

@recipe_router.get("/", status_code=status.HTTP_200_OK)
def get_recipes(params=Depends(dependency=standard_params)):
    return {"message": "List of recipes", "params": params, "data": [
        {"name": "Method 1", "ratio": "1:16", "grind_size": "Medium", "water_temp": 92.0, "bean_name": "Ethiopian", "bean_process": "Washed", "bean_roast_level": "Light", "bean_roast_date": "2024-01-01"},
    ]}


@recipe_router.post("/", status_code=status.HTTP_201_CREATED)
def create_recipe(body: RecipeRequest):
    return RecipeResponse(
        id="recipe_123",
        name= "New Recipe",
        ratio= "1:15",
        grind_size= "Medium-Fine",
        water_temp= 92.0,
        bean_name= "Ethiopian",
        bean_process= "Washed",
        bean_roast_level= "Light",
        bean_roast_date= "2024-01-01",
    )