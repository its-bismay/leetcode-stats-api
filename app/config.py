from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    LEETCODE_GRAPHQL_URL: str = "https://leetcode.com/graphql"
    APP_NAME: str = "LeetCode Stats API"
    DEBUG: bool = False

    class Config:
        env_file = ".env"

settings = Settings()