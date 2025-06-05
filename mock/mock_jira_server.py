
from flask import Flask, jsonify
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)

MOCK_ISSUES = {
    "PROJ-101": {
        "key": "PROJ-101",
        "fields": {
            "summary": "Login page not responsive",
            "status": {"name": "To Do"}
        }
    },
    "PROJ-102": {
        "key": "PROJ-102",
        "fields": {
            "summary": "API returns 500 error on POST",
            "status": {"name": "In Progress"}
        }
    },
    "PROJ-103": {
        "key": "PROJ-103",
        "fields": {
            "summary": "Update footer styling",
            "status": {"name": "Done"}
        }
    }
}

@app.route('/rest/api/3/issue/<issue_key>', methods=['GET'])
def get_issue(issue_key):
    issue = MOCK_ISSUES.get(issue_key)
    if issue:
        logging.info(f"Mock issue returned for {issue_key}")
        return jsonify(issue), 200
    else:
        logging.warning(f"Mock issue not found for {issue_key}")
        return jsonify({"error": "Issue not found"}), 404

if __name__ == '__main__':
    logging.info("Starting mock JIRA server at http://localhost:5001")
    app.run(port=5001)
