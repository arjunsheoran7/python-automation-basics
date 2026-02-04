incidents = ["low", "high", "medium", "high"]

for incident in incidents:
    incident = incident.strip().lower()
    if incident == "high":
        print("Escalate incident")
    else:
        print("Handle normally")