from fastapi import APIRouter, HTTPException, Depends, status, Path, Query
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db


router = APIRouter(prefix='contacts', tags=['contacts'])

@router.get("/")
async def get_todos():
    pass


@router.get("/{contact_id}")
async def get_contact():
    pass


@router.post("/")
async def create_contact():
    pass


@router.put("/{contact_id}")
async def update_contact():
    pass


@router.delete("/{contact_id}")
async def delete_contact():
    pass