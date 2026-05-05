from pydantic import BaseModel

class ProblemCount(BaseModel):
    total: int
    easy: int
    medium: int
    hard: int

class BasicResponse(BaseModel):
    username: str
    global_rank: int
    problems: ProblemCount