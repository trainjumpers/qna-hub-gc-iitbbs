import pytest
from httpx import AsyncClient
from fastapi import status

from app.main import app


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=app, base_url='http://localhost:8000') as ac:
        response = await ac.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "message": "Welcome to our discussion forum meant for GC Hackathon participants and a few special creatures"
    }
