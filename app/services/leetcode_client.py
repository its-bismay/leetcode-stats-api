import httpx
import asyncio
from app.config import settings
from app.core.exceptions import UserNotFoundException, LeetCodeAPIError

HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://leetcode.com",
}

PROFILE_QUERY = """
    query getUserProfile($username: String!) {
        matchedUser(username: $username) {
            username
            submitStats: submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
            profile {
                ranking
            }
            tagProblemCounts {
                advanced {
                    tagName
                    problemsSolved
                }
                intermediate {
                    tagName
                    problemsSolved
                }
                fundamental {
                    tagName
                    problemsSolved
                }
            }
        }
    }
"""

CONTEST_QUERY = """
    query userContestRanking($username: String!) {
        userContestRanking(username: $username) {
            rating
            globalRanking
            totalParticipants
            topPercentage
            attendedContestsCount
        }
    }
"""

CALENDAR_QUERY = """
    query userProfileCalendar($username: String!) {
        matchedUser(username: $username) {
            userCalendar {
                submissionCalendar
            }
        }
    }
"""


async def fetch_all_stats(username: str) -> tuple[dict, dict]:
    profile_payload = {"query": PROFILE_QUERY, "variables": {"username": username}}
    contest_payload = {"query": CONTEST_QUERY, "variables": {"username": username}}

    try:
        async with httpx.AsyncClient() as client:
            profile_res, contest_res = await asyncio.gather(
                client.post(settings.LEETCODE_GRAPHQL_URL, json=profile_payload, headers=HEADERS),
                client.post(settings.LEETCODE_GRAPHQL_URL, json=contest_payload, headers=HEADERS),
            )

        profile_data = profile_res.json()
        contest_data = contest_res.json()

    except httpx.RequestError:
        raise LeetCodeAPIError()

    user = profile_data.get("data", {}).get("matchedUser")
    if not user:
        raise UserNotFoundException(username)

    contest = contest_data.get("data", {}).get("userContestRanking")

    return user, contest



async def fetch_calendar(username: str) -> str:
    payload = {"query": CALENDAR_QUERY, "variables": {"username": username}}

    try:
        async with httpx.AsyncClient() as client:
            res = await client.post(settings.LEETCODE_GRAPHQL_URL, json=payload, headers=HEADERS)
        data = res.json()
    except httpx.RequestError:
        raise LeetCodeAPIError()

    user = data.get("data", {}).get("matchedUser")
    if not user:
        raise UserNotFoundException(username)

    return user["userCalendar"]["submissionCalendar"]