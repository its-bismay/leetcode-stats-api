from pydantic import BaseModel

class ContestResponse(BaseModel):
    username: str
    available: bool
    rating: int | None = None
    global_ranking: int | None = None
    total_participants: int | None = None
    top_percentage: float | None = None
    contests_attended: int | None = None