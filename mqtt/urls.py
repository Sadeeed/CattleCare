from django.urls import path
from mqtt.views import IndexView, DbToCSVView, DashboardView, DashboardDetailsView, ProfileView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('dashboard/details/', DashboardDetailsView.as_view(), name='dashboard-details'),
    path('dashboard/details/', DashboardDetailsView.as_view(), name='dashboard-details'),
    path('dashboard/profile/', ProfileView.as_view(), name='dashboard-profile'),
    path('csv/', DbToCSVView.as_view(), name='csv'),
]
