import csv
from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import mqtt
from .models import CollarData


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        mqtt.client.loop_start()
        context["temperature"] = CollarData.objects.filter(topic='collar/temperature').last()
        context["bellowing"] = CollarData.objects.filter(topic='collar/bellowing').last()
        context["X"] = CollarData.objects.filter(topic='collar/accel/X').last()
        context["Y"] = CollarData.objects.filter(topic='collar/accel/Y').last()
        context["Z"] = CollarData.objects.filter(topic='collar/accel/Z').last()
        context["bpm"] = CollarData.objects.filter(topic='collar/bpm').last()
        return self.render_to_response(context)


class dbToCSVView(TemplateView):
    template_name = 'temp.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        temperature = CollarData.objects.filter(topic='collar/temperature').all()
        bellowing = CollarData.objects.filter(topic='collar/bellowing').all()
        x = CollarData.objects.filter(topic='collar/accel/X').all()
        y = CollarData.objects.filter(topic='collar/accel/Y').all()
        z = CollarData.objects.filter(topic='collar/accel/Z').all()
        bpm = CollarData.objects.filter(topic='collar/bpm').all()
        gas = CollarData.objects.filter(topic='collar/ketosis').all()
        leg = CollarData.objects.filter(topic='leg/mvmt/').all()

        count = 1

        with open(f'dataset-{datetime.today().date()}.csv', 'w') as csvfile:
            csvfile = csv.writer(csvfile)
            csvfile.writerow(['#', 'temperature', 'bellowing', 'x', 'y', 'z', 'bpm', 'gas', 'leg'])
            for t, b, x, y, z, bp, g, l in zip(temperature, bellowing, x, y, z, bpm, gas, leg):
                csvfile.writerow(
                    [count, t.message, b.message, x.message, y.message, z.message, bp.message, g.message, l.message])
                count += 1
        return self.render_to_response(context)
