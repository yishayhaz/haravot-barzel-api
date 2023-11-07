from dotenv import load_dotenv
from fastapi import FastAPI
import routes
from helpers.env import EnvVars

load_dotenv()

app = FastAPI()

app.include_router(routes.router)

if __name__ == "__main__":
    import uvicorn

    if EnvVars.CREATE_INDEXES:
        import db

        db.create_indexes()

    uvicorn.run(
        "main:app",
        reload=True,
        host="0.0.0.0"
    )