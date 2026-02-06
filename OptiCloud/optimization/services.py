from django.db.models import Avg, Sum
from .models import ResourceUsage

def analyze_resource_usage():
    analysis = []

    resources = (
        ResourceUsage.objects
        .values("resource_id")
        .annotate(
            avg_cpu=Avg("cpu_usage"),
            avg_memory=Avg("memory_usage"),
            total_cost=Sum("cost")
        )
    )

    for r in resources:
        status = "EFFICIENT"
        wasted_cost = 0

        if r["avg_cpu"] < 20 and r["avg_memory"] < 25:
            status = "UNDERUTILIZED"
            wasted_cost = r["total_cost"] * 0.4  # estimated waste

        elif r["avg_cpu"] > 80:
            status = "OVERUTILIZED"

        analysis.append({
            "resource_id": r["resource_id"],
            "avg_cpu": round(r["avg_cpu"], 2),
            "avg_memory": round(r["avg_memory"], 2),
            "total_cost": round(r["total_cost"], 2),
            "status": status,
            "wasted_cost": round(wasted_cost, 2)
        })

    return analysis
