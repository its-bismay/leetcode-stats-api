import json
from datetime import datetime, timezone, timedelta


def parse_basic(user: dict) -> dict:
    stats = user["submitStats"]["acSubmissionNum"]

    return {
        "username": user["username"],
        "global_rank": user["profile"]["ranking"],
        "problems": {
            "total":  next((s["count"] for s in stats if s["difficulty"] == "All"),    0),
            "easy":   next((s["count"] for s in stats if s["difficulty"] == "Easy"),   0),
            "medium": next((s["count"] for s in stats if s["difficulty"] == "Medium"), 0),
            "hard":   next((s["count"] for s in stats if s["difficulty"] == "Hard"),   0),
        }
    }


def parse_contest(username: str, contest: dict | None) -> dict:
    if not contest:
        return {
            "username": username,
            "available": False,
        }

    return {
        "username": username,
        "available": True,
        "rating": round(contest["rating"]),
        "global_ranking": contest["globalRanking"],
        "total_participants": contest["totalParticipants"],
        "top_percentage": round(contest["topPercentage"], 2),
        "contests_attended": contest["attendedContestsCount"],
    }


def parse_topics(user: dict) -> dict:
    tags = user["tagProblemCounts"]

    all_topics = [
        *tags["fundamental"],
        *tags["intermediate"],
        *tags["advanced"],
    ]

    sorted_topics = sorted(all_topics, key=lambda t: t["problemsSolved"], reverse=True)

    return {
        "username": user["username"],
        "topics": [
            {"name": t["tagName"], "problems_solved": t["problemsSolved"]}
            for t in sorted_topics
        ]
    }


def parse_last_seven_days(username: str, raw_calendar: str) -> dict:
    calendar: dict = json.loads(raw_calendar)

    today = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)

    last_seven = []
    for i in range(6, -1, -1):
        day = today - timedelta(days=i)
        timestamp = str(int(day.timestamp()))
        last_seven.append({
            "date": day.strftime("%Y-%m-%d"),
            "submissions": calendar.get(timestamp, 0)
        })

    total = sum(d["submissions"] for d in last_seven)

    return {
        "username": username,
        "last_7_days": last_seven,
        "total_submissions": total,
    }


def parse_all(user: dict, contest: dict | None, raw_calendar: str) -> dict:
    return {
        **parse_basic(user),
        "contest": parse_contest(user["username"], contest),
        "topics": parse_topics(user)["topics"],
        **parse_last_seven_days(user["username"], raw_calendar),
    }