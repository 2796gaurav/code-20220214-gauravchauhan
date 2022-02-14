from fastapi.testclient import TestClient
import sys

sys.path.append(".")
from .main import app

client = TestClient(app)


def test_sol1_input_field():
    """
    test on solution1 to check if input/output file data type provided incorrect
    """
    response = client.post(
        "/solution1/",
        json={"input_location": "data.csv", "output_location": "output_data.csv"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input/ output file type"}


def test_sol1_data_io_size():
    """
    test on solution1 to check input users data = output users data
    """
    response = client.post(
        "/solution1/",
        json={"input_location": "data.json", "output_location": "output_data.csv"},
    )

    c = 6
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "msg": "updated solution to output file",
        "records": c,
    }


def test_sol1_json_file_present():
    """
    test on solution1 to check if input json file present or is in correct order
    """
    response = client.post(
        "/solution1/",
        json={"input_location": "data_test.json", "output_location": "output_data.csv"},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Not found Json file or Json file format incorrect."
    }


def test_sol2_input_field():
    """
    test on solution2 to check if input file data type provided incorrect
    """
    response = client.get("/solution2/out.json")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input file type"}


def test_sol2_data_io_size():
    """
    test on solution2 to check if the ourput provided is correct.
    """
    response = client.get("/solution2/out.csv")
    assert response.status_code == 200
    c = 1
    assert response.json() == {"count": c}
