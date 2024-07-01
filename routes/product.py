from fastapi import APIRouter


product_router = APIRouter()

@product_router.get('/samsung')
def samsung():
    return {'samsung': 'samsung'}

