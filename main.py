from dotenv import load_dotenv
from fastapi import FastAPI
import routes
from helpers.env import EnvVars

load_dotenv()

app = FastAPI()

app.include_router(routes.router)