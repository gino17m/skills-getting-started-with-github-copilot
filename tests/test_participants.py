from fastapi.testclient import TestClient

from src.app import app, activities


client = TestClient(app)


def test_unregister_participant_from_activity():
    activity_name = "Chess Club"
    activity = activities[activity_name]
    original_participants = list(activity["participants"])
    email = original_participants[0]

    response = client.delete(f"/activities/{activity_name}/participants/{email}")

    assert response.status_code == 200
    assert email not in activity["participants"]
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"

    activity["participants"] = original_participants
