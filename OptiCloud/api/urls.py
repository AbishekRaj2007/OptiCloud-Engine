from django.urls import path
from .views import HealthView, CostAnomalyView

urlpatterns = [
    path("health/", HealthView.as_view()),
    path("cost/anomaly/", CostAnomalyView.as_view()),
]
