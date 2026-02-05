def recommend_rightsizing(cpu_usage, memory_usage):
    if cpu_usage < 20 and memory_usage < 30:
        action = "downsize"
        reason = "Resource is underutilized"
    elif cpu_usage > 80 or memory_usage > 80:
        action = "scale_up"
        reason = "Resource is close to capacity"
    else:
        action = "keep"
        reason = "Resource usage is optimal"

    return {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_usage,
        "recommendation": action,
        "reason": reason
    }