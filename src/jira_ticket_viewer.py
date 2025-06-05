# Version: v0.2.2

import logging
from flask import Flask, render_template_string
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

# Config from .env or fallback to mock
JIRA_URL = os.getenv("JIRA_URL", "http://localhost:5001")
JIRA_EMAIL = os.getenv("JIRA_EMAIL", "mock@example.com")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "mock-token")

HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

TEMPLATE = """
<!DOCTYPE html>
<html>
<head><title>JIRA Ticket Viewer</title></head>
<body>
    <h1>JIRA Ticket Details</h1>
    <table border="1">
        <tr><th>Key</th><th>Summary</th><th>Status</th></tr>
        {% for issue in issues %}
        <tr>
            <td>{{ issue.key }}</td>
            <td>{{ issue.fields.summary }}</td>
            <td>{{ issue.fields.status.name }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def read_ticket_codes(filepath):
    try:
        with open(filepath, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    except Exception as e:
        logging.error(f"Failed to read ticket codes: {e}")
        return []

def fetch_jira_issues(ticket_codes):
    issues = []
    auth = (JIRA_EMAIL, JIRA_API_TOKEN)
    for code in ticket_codes:
        try:
            url = f"{JIRA_URL}/rest/api/3/issue/{code}"
            response = requests.get(url, headers=HEADERS, auth=auth)
            if response.status_code == 200:
                issues.append(response.json())
                logging.info(f"Fetched issue: {code}")
            else:
                logging.warning(f"Failed to fetch {code}: {response.status_code}")
        except Exception as e:
            logging.error(f"Error fetching {code}: {e}")
    return issues

@app.route('/')
def index():
    ticket_codes = read_ticket_codes("mock/tickets.txt")
    raw_issues = fetch_jira_issues(ticket_codes)
    return render_template_string(TEMPLATE, issues=raw_issues)

if __name__ == '__main__':
    logging.info("Starting Flask server on http://localhost:5000")
    app.run(debug=True)