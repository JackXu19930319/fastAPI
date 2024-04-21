import uvicorn
from fastapi import FastAPI
from routes.user import router as users_router

app = FastAPI()

app.include_router(users_router, prefix="/api/v1/users", tags=["users"])

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
