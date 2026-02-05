from rest_framework.views import APIView
from rest_framework.response import Response
from cost_analysis.services.anomaly_detector import detect_cost_anomaly
from optimization.services.rightsizing import recommend_rightsizing
from decision_engine.services.engine import make_decision
from optimization.services.rightsizing import recommend_rightsizing
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
    
class RightSizingView(APIView):
    def get(self, request):
        result = recommend_rightsizing(
            cpu_usage=15,
            memory_usage=22
        )
        return Response(result)
    
class DecisionView(APIView):
    def get(self, request):
        cost_result = detect_cost_anomaly(
            today_cost=310,
            past_costs=[120, 130, 125, 118, 122, 119, 121]
        )

        rightsizing_result = recommend_rightsizing(
            cpu_usage=15,
            memory_usage=22
        )

        decision = make_decision(cost_result, rightsizing_result)

        return Response({
            "cost_analysis": cost_result,
            "rightsizing": rightsizing_result,
            "final_decision": decision
        })
