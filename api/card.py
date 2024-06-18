from fastapi import APIRouter, status, Depends
from schames import ProductBase
from database import engine, session
from model import Product, Users, Cart
from fastapi.exceptions import HTTPException
from fastapi.encoders import jsonable_encoder
from fastapi_jwt_auth import AuthJWT

session = session(bind=engine)

card_router = APIRouter(prefix="/orders")


@card_router.get('/')
async def select(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token")
    cards = session.query(Cart).all()
    context = [
        {
            "id": card.id,
            "Product": {
                "id": card.title_id.id,
                "username": card.title_id.product_name,
                "email": card.title_id.description,
                "count": card.title_id.count
            },

            "User": {
                "id": card.user_id.id,
                "name": card.user_id.first_name,
                "price": card.user_id.last_name
            },
        }
        for card in cards
    ]
    return jsonable_encoder(context)


