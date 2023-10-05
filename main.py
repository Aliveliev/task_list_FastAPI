import uvicorn
from fastapi import FastAPI

from database import SessionLocal, engine, Base
from routers import task as TaskRouter

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(TaskRouter.router, prefix='/tasks')


if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

