from app.routers.auth import auth_router
from app.routers.roasteries import roastery_router
from sys import prefix
from app.routers.recipes import recipe_router
from fastapi import FastAPI


from app.core.settings import settings
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(
    title = settings.APP_NAME,
    version = settings.VERSION,
)

app.include_router(router=auth_router, prefix="/api")
app.include_router(router=recipe_router, prefix="/api")
app.include_router(router=roastery_router, prefix="/api")


@app.get("/scalar")
def get_scalar():
    return get_scalar_api_reference(
        openapi_url= app.openapi_url,
        title= app.title
    )