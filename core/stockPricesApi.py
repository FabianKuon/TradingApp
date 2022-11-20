from fastapi import APIRouter

router = APIRouter()


@router.get("/stocks/{stock}")
async def getPriceForStock(stock: str):
    return {'stock': stock}
