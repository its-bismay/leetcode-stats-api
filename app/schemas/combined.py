from pydantic import BaseModel
from app.schemas.problems import ProblemCount
from app.schemas.contest import ContestResponse
from app.schemas.topics import TopicStat

class AllStatsResponse(BaseModel):
    username: str
    global_rank: int
    problems: ProblemCount
    contest: ContestResponse
    topics: list[TopicStat]