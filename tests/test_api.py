import pytest
from app import app


@pytest.fixture
def application():
    yield app


@pytest.fixture
def client(application):
    return application.test_client()


@pytest.mark.parametrize(
    "chess_figure", ["pawn", "knight", "bishop", "rook", "queen", "king"]
)
def test_correct_figure_url(client, chess_figure):
    response = client.get(f"/api/v1/{chess_figure}/a2/")
    data = response.json
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data.get("availableMoves"), list)
    assert isinstance(data.get("figure"), str)
    assert isinstance(data.get("currentField"), str)


def test_valid_move_url(client):
    response = client.get("/api/v1/pawn/a2/a3/")
    data = response.json
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert isinstance(data.get("move"), str)
    assert isinstance(data.get("figure"), str)
    assert isinstance(data.get("currentField"), str)
    assert isinstance(data.get("destField"), str)
    assert data.get("move") == "valid"


def test_invalid_move_url(client):
    response = client.get("/api/v1/pawn/a2/a1/")
    data = response.json
    assert response.status_code == 409
    assert isinstance(data, dict)
    assert isinstance(data.get("move"), str)
    assert isinstance(data.get("figure"), str)
    assert isinstance(data.get("error"), str)
    assert isinstance(data.get("currentField"), str)
    assert isinstance(data.get("destField"), str)
    assert data.get("move") == "invalid"


@pytest.mark.parametrize("chess_figure", ["pawns", "hello"])
def test_incorrect_figure_url(client, chess_figure):
    response = client.get(f"/api/v1/{chess_figure}/a2/")
    data = response.json
    assert response.status_code == 404
    assert isinstance(data, dict)
    assert isinstance(data.get("availableMoves"), list)
    assert isinstance(data.get("error"), str)
    assert isinstance(data.get("figure"), str)
    assert isinstance(data.get("currentField"), str)


@pytest.mark.parametrize("current_field", ["a22", "b9"])
def test_incorrect_current_field_url(client, current_field):
    response = client.get(f"/api/v1/pawn/{current_field}/")
    data = response.json
    assert response.status_code == 409
    assert isinstance(data, dict)
    assert isinstance(data.get("availableMoves"), list)
    assert isinstance(data.get("error"), str)
    assert isinstance(data.get("figure"), str)
    assert isinstance(data.get("currentField"), str)
    assert data.get("error") == "Field does not exist."


@pytest.mark.parametrize("dest_field", ["z1", "x2"])
def test_incorrect_dest_field_url(client, dest_field):
    response = client.get(f"/api/v1/pawn/a2/{dest_field}/")
    data = response.json
    assert response.status_code == 409
    assert isinstance(data, dict)
    assert isinstance(data.get("move"), str)
    assert isinstance(data.get("error"), str)
    assert isinstance(data.get("figure"), str)
    assert isinstance(data.get("currentField"), str)
    assert isinstance(data.get("destField"), str)
    assert data.get("error") == "Destination field does not exist"


def test_page_not_found(client):
    response = client.get("/hello/")
    assert response.status_code == 404
