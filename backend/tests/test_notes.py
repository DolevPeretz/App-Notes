import pytest
from httpx import AsyncClient
from tests.utils import get_access_token

email = "test@example.com"
password = "123456"

@pytest.mark.asyncio
async def test_notes_crud_flow():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        token = await get_access_token(ac, email, password)
        headers = {"Authorization": f"Bearer {token}"}

        note_data = {"title": "My test note", "content": "This is a test note"}
        create_res = await ac.post(
            url="/notes/",
            json=note_data,
            headers=headers
        )

        print(create_res.status_code)
        print(create_res.headers)
        print(create_res.text)
        assert create_res.status_code == 200
        note = create_res.json()
        note_id = note["id"]
        assert note["title"] == "My test note"

        get_res = await ac.get("/notes/", headers=headers)
        assert get_res.status_code == 200
        notes = get_res.json()
        assert any(n["id"] == note_id for n in notes)

        updated = {"title": "Updated Title", "content": "Updated content"}
        update_res = await ac.put(f"/notes/{note_id}", json=updated, headers=headers)
        assert update_res.status_code == 200
        assert update_res.json()["title"] == "Updated Title"

        delete_res = await ac.delete(f"/notes/{note_id}", headers=headers)
        assert delete_res.status_code == 200

        get_res_after = await ac.get("/notes/", headers=headers)
        assert all(n["id"] != note_id for n in get_res_after.json())
