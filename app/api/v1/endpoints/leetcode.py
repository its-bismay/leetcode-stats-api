from fastapi import APIRouter
from app.services.leetcode_client import fetch_all_stats
from app.services.stats_parser import parse_basic, parse_contest, parse_topics, parse_all
from app.schemas.problems import BasicResponse
from app.schemas.contest import ContestResponse
from app.schemas.topics import TopicsResponse
from app.schemas.combined import AllStatsResponse

router = APIRouter(prefix="/{username}", tags=["LeetCode"])


@router.get("/all", response_model=AllStatsResponse)
async def get_all_stats(username: str):
    user, contest = await fetch_all_stats(username)
    return parse_all(user, contest)


@router.get("/basic", response_model=BasicResponse)
async def get_basic_stats(username: str):
    user, _ = await fetch_all_stats(username)
    return parse_basic(user)


@router.get("/contest", response_model=ContestResponse)
async def get_contest_stats(username: str):
    user, contest = await fetch_all_stats(username)
    return parse_contest(user["username"], contest)


@router.get("/topics", response_model=TopicsResponse)
async def get_topics(username: str):
    user, _ = await fetch_all_stats(username)
    return parse_topics(user)