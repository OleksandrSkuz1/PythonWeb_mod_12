from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.routes import contacts
from src.routes import auth


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Contact Application"}
