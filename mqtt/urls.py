from django.urls import path
from mqtt.views import IndexView, dbToCSVView, DashboardView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('csv/', dbToCSVView.as_view(), name='csv'),
]
