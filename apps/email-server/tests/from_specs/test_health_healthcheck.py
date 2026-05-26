"""Tests derived from specs/features/health/healthcheck.spec.yaml"""

from email_server.api.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_healthz_returns_200() -> None:
    """spec: health/healthcheck — Then: Status HTTP é 200"""
    response = client.get("/healthz")
    assert response.status_code == 200


def test_healthz_returns_status_ok() -> None:
    """spec: health/healthcheck — Then: Body contém status ok"""
    response = client.get("/healthz")
    assert response.json() == {"status": "ok"}
