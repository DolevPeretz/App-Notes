
from httpx import AsyncClient
from app.main import app
import pytest

@pytest.mark.asyncio
async def test_login_success():
    async with AsyncClient( base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post("/auth/login", json={
            "email": "test@example.com",
            "password": "123456"
        })
    assert response.status_code == 200
    assert "access_token" in response.json()
