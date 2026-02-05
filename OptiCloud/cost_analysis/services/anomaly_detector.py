def detect_cost_anomaly(today_cost, past_costs):
    average = sum(past_costs) / len(past_costs)
    spike_percentage = ((today_cost - average) / average) * 100

    return {
        "today_cost": today_cost,
        "average_cost": round(average, 2),
        "spike_percentage": round(spike_percentage, 2),
        "anomaly": spike_percentage > 40
    }
