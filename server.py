from fastapi import FastAPI
from app.config import settings
from app.api.v1.router import router as api_router

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": f"{settings.APP_NAME} is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
