# Version: v0.2.1

import requests

def test_mock_jira_issues():
    mock_url = "http://localhost:5001"
    codes = {
        "PROJ-101": 200,
        "PROJ-102": 200,
        "PROJ-103": 200,
        "INVALID-999": 404
    }

    for code, expected_status in codes.items():
        resp = requests.get(f"{mock_url}/rest/api/3/issue/{code}")
        assert resp.status_code == expected_status, f"{code} failed with {resp.status_code}"