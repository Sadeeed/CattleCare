from django.urls import path
from mqtt.views import IndexView, dbtoCSVView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('csv/', dbtoCSVView.as_view(), name='csv'),
]
