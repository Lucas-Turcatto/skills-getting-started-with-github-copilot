from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    email = "test-student@mergington.edu"

    signup_response = client.post(
        "/activities/{activity_name}/signup".format(activity_name=activity_name),
        params={"email": email},
    )
    assert signup_response.status_code == 200

    delete_response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )
    assert delete_response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
