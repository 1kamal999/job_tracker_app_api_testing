import re

import requests

from configs.settings import BASE_URL



'''
{
  "app_name": "SuperSQA Job Tracker",
  "api_version": "v1",
  "environment": "local",
  "server_time": "2026-11-22T23:35:44.496650Z"
}
'''
def test_public_status_endpoint():  
    url = f"{BASE_URL}/api/v1/public/status"
    response = requests.get(url)
    response_body = response.json()
   
    # print("Response status code:", response.status_code)

    # print("Testing public status endpoint")
    assert response.status_code == 200
    assert response_body["app_name"] == "SuperSQA Job Tracker"
    assert response_body["api_version"] == "v1"
    assert response_body["environment"] == "local"
    assert "server_time" in response_body
    assert re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z",
        response_body["server_time"],
    )

''' asample response for public stats endpoint{
  "total_seeded_applications": 4,
  "status_counts": {
    "potential": 2,
    "applied": 1,
    "in_progress": 1,
    "final_stage": 0,
    "hired": 0,
    "rejected": 0,
    "withdrawn": 0,
    "total": 4
  }
}'''


def test_public_stats_endpoint():
        url = f"{BASE_URL}/api/v1/public/demo-stats"
        response = requests.get(url)
        response_body = response.json()

        assert response.status_code == 200
        assert "total_seeded_applications" in response_body
        assert "status_counts" in response_body
        assert isinstance(response_body["total_seeded_applications"], int)
        assert isinstance(response_body["status_counts"], dict)
        for k,v in response_body["status_counts"].items():
            assert isinstance(v, int)