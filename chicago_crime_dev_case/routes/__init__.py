from fastapi import APIRouter

from .profile import router as profile_router
from .security import router as security_router
from .user import router as user_router
from .chicago_crimes import router as chicago_crimes_router

main_router = APIRouter()
main_router.include_router(profile_router, tags=["user"])
main_router.include_router(security_router, tags=["security"])
main_router.include_router(user_router, prefix="/user", tags=["user"])
main_router.include_router(chicago_crimes_router, prefix="/chicago_crimes", tags=["chicago_crimes"])


@main_router.get("/")
async def index():
    return {"message": "Hello World!"}