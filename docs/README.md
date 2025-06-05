# JIRA Ticket Viewer

## Version: v0.2.1

### Description
A Python Flask app to display JIRA tickets from a list. Includes mock server for testing.

### Requirements
- Python 3.8+
- Flask
- requests
- pytest

### Setup

1. Install dependencies:
```bash
pip install flask requests pytest
```

2. Set environment variables (for real JIRA access):
```bash
export JIRA_URL=https://your-domain.atlassian.net
export JIRA_EMAIL=you@example.com
export JIRA_API_TOKEN=your_api_token
```

3. To use mock server:
```bash
python mock_jira_server.py
```

4. Run the main app:
```bash
python jira_ticket_viewer.py
```

5. Run tests:
```bash
pytest test_app.py
```

### Files
- `jira_ticket_viewer.py`: Main app
- `mock_jira_server.py`: Local mock JIRA API
- `tickets.txt`: Input file for ticket codes
- `test_app.py`: Test suite for verifying responses