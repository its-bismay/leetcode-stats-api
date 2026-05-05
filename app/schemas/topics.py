from pydantic import BaseModel

class TopicStat(BaseModel):
    name: str
    problems_solved: int

class TopicsResponse(BaseModel):
    username: str
    topics: list[TopicStat]