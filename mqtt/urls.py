from django.urls import path
from mqtt.views import IndexView, dbToCSVView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('csv/', dbToCSVView.as_view(), name='csv'),
]
