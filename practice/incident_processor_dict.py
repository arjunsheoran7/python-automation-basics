INCIDENT_ACTIONS = {
    "low": "Handle normally",
    "medium": "Notify regional manager",
    "high": "Escalate incident"
}

def process_incident(severity):
    severity = severity.strip().lower()

    action = INCIDENT_ACTIONS.get(severity)

    if action is None:
        print("ERROR: Unknown severity ->", severity)
        return "Invalid severity"

    return action


incidents = ["Low", "HIGH ", "medium", "high", "critical", " Medium"]

for incident in incidents:
    action = process_incident(incident)
    print(action)