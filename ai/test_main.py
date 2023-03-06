import json
import pytest

from httpx import AsyncClient
from fastapi.testclient import TestClient

import main
client = TestClient(main.app)



@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/test/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}


@pytest.mark.asyncio
async def test_read_item():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/test/items/foo", params={"item_id": "1"})
        assert response.status_code == 200
        assert response.json() == {
            "id": "foo",
            "title": "Foo",
            "description": "There goes my hero",
        }


@pytest.mark.asyncio
async def test_create_item():
    async with AsyncClient(base_url="http://127.0.0.1:8000") as ac:
        response = await ac.post(
            "/test/items/",
            content=json.dumps(
                {
                    "id": "foobar",
                    "title": "Foo Bar",
                    "description": "The Foo Barters",
                }
            ),
        )
        assert response.status_code == 200
        assert response.json() == {
            "id": "foobar",
            "title": "Foo Bar",
            "description": "The Foo Barters",
        }


def test_check():
    response = client.get("/get/test_1")
    assert response.status_code == 200
    assert response.json() == {'result':'test'}

def test_first_get():
    response = client.get("/get/test_2")
    assert response.status_code == 200
    assert response.json() == {'result':'test'}