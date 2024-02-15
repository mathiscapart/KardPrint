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


def test_print():
    response = client.post("/v1/printer/print")
    assert response.status_code == 200
    assert response.json() == {
        "printer": "print"
    }


def test_add_card_to_spooler():
    response = client.post("/v1/printer/spooler/544")
    assert response.status_code == 200
    assert response.json() == {
        'spooler': 'add 544'
    }


def test_bad_add_card_to_spooler():
    card = client.get("/v1/printer/spooler/first")
    card_result = card.json()
    response = client.post(f"/v1/printer/spooler/{card_result["spooler"]}")
    assert response.status_code == 500
    assert response.json() == {
        'result': 'Card is already in spooler'
    }


def test_ink_level():
    response = client.get(f"/v1/printer/ink")
    assert response.status_code == 200
    assert response.json() == {
        "black": 100,
        "cyan": 100,
        "magenta": 100,
        "yellow": 100
    }
