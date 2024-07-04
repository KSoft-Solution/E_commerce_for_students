from fastapi import APIRouter
from models.product import Product

product_router = APIRouter(prefix="/product",tags=['product'])

@product_router.get('/samsung')
def samsung():
    return {'samsung': 'samsung'}

@product_router.post('/create')
def create_product(data:Product):
    print(data)
    return {
        'response': "success"
    }

