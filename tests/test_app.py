from fastapi.testclient import TestClient

from src.app import app


def test_unregister_participant_removes_email_from_activity():
    with TestClient(app) as client:
        signup_response = client.post(
            "/activities/Chess Club/signup?email=test@example.com"
        )
        assert signup_response.status_code == 200

        remove_response = client.delete(
            "/activities/Chess Club/signup?email=test@example.com"
        )
        assert remove_response.status_code == 200

        activities_response = client.get("/activities")
        assert activities_response.status_code == 200
        activity = activities_response.json()["Chess Club"]
        assert "test@example.com" not in activity["participants"]
