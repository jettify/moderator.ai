import pytest
from aiohttp import web


async def test_index_page(api):
    resp = await api.get('/')
    assert resp.status == 200
    body = await resp.text()
    assert "" in body


async def test_moderate(api):
    payload = {"body": "xxx", "model_type": "LR"}
    resp = await api.post('/moderate', json=payload)
    assert resp.status == 200
    data = await resp.json()
    expected = {'identity_hate': 0.5,
                'insult': 0.5,
                'threat': 0.5,
                'toxic': 0.5}
    assert data == expected
