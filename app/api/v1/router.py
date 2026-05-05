from fastapi import APIRouter
from app.api.v1.endpoints.leetcode import router as leetcode_router

router = APIRouter(prefix="/api/v1/leetcode")
router.include_router(leetcode_router)