from django.urls import path
from .views import HealthView, CostAnomalyView
from .views import RightSizingView
from .views import DecisionView
urlpatterns = [
    path("health/", HealthView.as_view()),
    path("cost/anomaly/", CostAnomalyView.as_view()),
    path("resources/rightsizing/", RightSizingView.as_view()),
    path("decision/", DecisionView.as_view()),
]
