from django.urls import path
from mqtt.views import IndexView, DbToCSVView, DashboardView, DashboardDetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/details/', DashboardDetailsView.as_view(), name='dashboard-details'),
    path('csv/', DbToCSVView.as_view(), name='csv'),
]
