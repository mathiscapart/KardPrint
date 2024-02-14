from fastapi.testclient import TestClient
from unittest.mock import patch
from projet.apiPrinter import app

client = TestClient(app)


def test_get_printer():
    response = client.get("/v1/printer")
    assert response.status_code == 200
    assert response.json() == {
        "model": "Xerox Printer",
        "dpi": "1200",
        "card_type": "plastic"
    }


def test_good_post():
    response = client.post("/v1/printer/print/9334")
    assert response.status_code == 200
    assert response.json() == {
        "result": "success"
    }


def test_bad_post_in_spooler():
    response = client.post("/v1/printer/print/9334")
    assert response.status_code == 500
    assert response.json() == {
        "result": "failure",
        'message': 'Card is already in spooler'
    }
