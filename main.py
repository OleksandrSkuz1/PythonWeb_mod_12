import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.routes import contacts, auth

app = FastAPI()

# Налаштування логування
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("app.log"),  # Запис у файл
        logging.StreamHandler()  # Відображення у консолі
    ]
)

logger = logging.getLogger(__name__)

app.include_router(auth.router, prefix="/api")
app.include_router(contacts.router, prefix="/api")

@app.get("/")
def index():
    return {"message": "Contact Application"}

@app.get("/api/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        # Make request
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(status_code=500, detail="Database is not configured correctly")
        return {"message": "Welcome to FastAPI!"}
    except Exception as e:
        logger.error(f"Healthcheck error: {e}")
        raise HTTPException(status_code=500, detail="Error connecting to the database")
