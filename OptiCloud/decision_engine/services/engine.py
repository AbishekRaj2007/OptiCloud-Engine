def make_decision(cost_result, rightsizing_result):
    decision = "no_action"
    confidence = 0.5
    reason = "System operating within normal parameters"

    if cost_result["anomaly"] and rightsizing_result["recommendation"] == "downsize":
        decision = "scale_down"
        confidence = 0.87
        reason = "Cost anomaly detected with underutilized resources"

    elif rightsizing_result["recommendation"] == "scale_up":
        decision = "scale_up"
        confidence = 0.82
        reason = "High resource utilization detected"

    return {
        "decision": decision,
        "confidence": confidence,
        "reason": reason
    }
