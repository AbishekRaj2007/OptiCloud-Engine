from rest_framework.views import APIView
from rest_framework.response import Response
from cost_analysis.services.anomaly_detector import detect_cost_anomaly


class HealthView(APIView):
    def get(self, request):
        return Response({
            "status": "ok",
            "service": "OptiCloud Engine"
        })


class CostAnomalyView(APIView):
    def get(self, request):
        result = detect_cost_anomaly(
            today_cost=310,
            past_costs=[120, 130, 125, 118, 122, 119, 121]
        )
        return Response(result)
