from pydantic import BaseModel
from app.schemas.problems import ProblemCount
from app.schemas.contest import ContestResponse
from app.schemas.topics import TopicStat
from app.schemas.calendar import DailySubmission

class AllStatsResponse(BaseModel):
    username: str
    global_rank: int
    problems: ProblemCount
    contest: ContestResponse
    topics: list[TopicStat]
    last_7_days: list[DailySubmission]
    total_submissions: int