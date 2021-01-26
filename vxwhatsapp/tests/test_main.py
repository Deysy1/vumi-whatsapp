import pytest

from vxwhatsapp.main import app


@pytest.fixture
def test_client(loop, sanic_client):
    return loop.run_until_complete(sanic_client(app))


async def test_health(test_client):
    response = await test_client.get(app.url_for("health"))
    assert response.status == 200
    assert (await response.json()) == {"status": "ok"}


async def test_metrics(test_client):
    response = await test_client.get(app.url_for("metrics"))
    assert response.status == 200
    body = await response.text()
    assert "sanic_request_latency_sec" in body
