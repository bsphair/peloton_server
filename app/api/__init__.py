from fastapi import APIRouter, Depends

from app.api.endpoints.authorization import auth_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth")