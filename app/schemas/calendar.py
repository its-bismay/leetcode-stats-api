from pydantic import BaseModel

class DailySubmission(BaseModel):
    date: str
    submissions: int

class LastSevenDaysResponse(BaseModel):
    username: str
    last_7_days: list[DailySubmission]
    total_submissions: int