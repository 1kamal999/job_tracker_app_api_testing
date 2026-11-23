import re

import requests
url ='http://localhost:3050/api/v1/public/status'

'''
{
  "app_name": "SuperSQA Job Tracker",
  "api_version": "v1",
  "environment": "local",
  "server_time": "2026-11-22T23:35:44.496650Z"
}
'''
def test_public_status_endpoint():  
    response = requests.get(url)
    response_json = response.json()
   
    # print("Response status code:", response.status_code)

    # print("Testing public status endpoint")
    assert response.status_code == 200
    assert response_json["app_name"] == "SuperSQA Job Tracker"
    assert response_json["api_version"] == "v1"
    assert response_json["environment"] == "local"
    assert "server_time" in response_json
    assert re.fullmatch(
        r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}Z",
        response_json["server_time"],
    )