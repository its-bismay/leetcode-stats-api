from fastapi import HTTPException, status

class UserNotFoundException(HTTPException):
    def __init__(self, username: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"LeetCode user '{username}' not found.",
        )

class LeetCodeAPIError(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="Failed to reach LeetCode GraphQL API. Try again later.",
        )