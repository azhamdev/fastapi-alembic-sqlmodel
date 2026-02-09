from app.models.database import Recipe
from sqlmodel import select
from app.models.engine import get_db
from app.schema.recipes import RecipeRequest
from fastapi import APIRouter, Depends, status, HTTPException
from app.utils.query_params import standard_params

recipe_router = APIRouter(
    prefix="/recipes",
    tags=["recipes"],
)

@recipe_router.get("/", status_code=status.HTTP_200_OK)
def get_recipes(params=Depends(dependency=standard_params), db=Depends(dependency=get_db)):
    stmt = select(Recipe)
    result= db.exec(stmt)
    recipes = result.all()


    return {"total": len(recipes), "data": recipes}


@recipe_router.post("/", status_code=status.HTTP_201_CREATED)
def create_recipe(body: RecipeRequest, db=Depends(dependency=get_db)):
    try:
        new_recipe = Recipe(
        name=body.name,
        ratio=body.ratio or "1:15",
        grind_size=body.grind_size,
        water_temp=body.water_temp,
        bean_name=body.bean_name,
        bean_process=body.bean_process,
        bean_roast_level=body.bean_roast_level,
        bean_roast_date=body.bean_roast_date,
    )
        db.add(new_recipe)
        db.commit()
        db.refresh(new_recipe)

        return {"message": "Recipe created successfully", "recipe": new_recipe}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
