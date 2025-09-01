# tests/utils.py

from httpx import AsyncClient

async def get_access_token(ac: AsyncClient, email: str, password: str) -> str:
    response = await ac.post("/auth/login", json={
        "email": email,
        "password": password
    })
    assert response.status_code == 200
    return response.json()["access_token"]
