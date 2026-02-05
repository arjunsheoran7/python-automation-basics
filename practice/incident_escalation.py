def process_incident(incident):
    incident = incident.strip().lower()

    if incident == "high":
        return "Escalate incident"
    else:
        return "Handle normally"


incidents = ["low", "high", "medium", "high"]

for incident in incidents:
    result = process_incident(incident)
    print(result)
