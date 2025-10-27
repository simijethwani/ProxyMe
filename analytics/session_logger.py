import json
from datetime import datetime

def log_session(data, path="logs/session.json"):
    data["timestamp"] = datetime.now().isoformat()
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
