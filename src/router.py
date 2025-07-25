from fastapi import APIRouter
from src.http_client import CMCHTTPClient
from src.config import settings
from src.init import cmc_client

router = APIRouter(
    prefix='/currancy'
)



@router.get('')
async def get_currency():
    return await cmc_client.get_listings()


@router.get('/{currancy_id}')
async def get_cryptocurrency(currancy_id: int):
    return await cmc_client.get_currency(currancy_id)