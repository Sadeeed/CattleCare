from django.views.generic import TemplateView
from . import mqtt
from .models import CollarData


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        mqtt.client.loop_start()
        context["temperature"] = CollarData.objects.filter(topic='collar/temperature').last()
        context["bellowing"] = CollarData.objects.filter(topic='collar/bellowing').last()
        context["X"] = CollarData.objects.filter(topic='collar/accel/X').last()
        context["Y"] = CollarData.objects.filter(topic='collar/accel/Y').last()
        context["Z"] = CollarData.objects.filter(topic='collar/accel/Z').last()
        return self.render_to_response(context)
