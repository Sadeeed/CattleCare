import csv
import random
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from . import mqtt
from .models import CollarData


class IndexView(TemplateView):
    template_name = "index.html"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        temperature = CollarData.objects.filter(topic='collar/temperature')
        bellow = CollarData.objects.filter(topic='collar/bellowing')
        X = CollarData.objects.filter(topic='collar/accel/X')
        Y = CollarData.objects.filter(topic='collar/accel/Y')
        Z = CollarData.objects.filter(topic='collar/accel/Z')
        bpm = CollarData.objects.filter(topic='collar/bpm')
        ketosis = CollarData.objects.filter(topic='collar/ketosis')

        data = zip(X, Y, Z, temperature, bellow, bpm, ketosis)

        for x, y, z, t, b, hr, k in data:
            print(f"[{x}, {y}, {z}, {t}, {b}, {hr}, {k}]")

        return self.render_to_response(context)


class DashboardDetailsView(TemplateView):
    template_name = 'dashboard/pages/details.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        mqtt.client.loop_start()
        context["temperature"] = CollarData.objects.filter(topic='collar/temperature').last()
        context["bellowing"] = CollarData.objects.filter(topic='collar/bellowing').last()
        context["X"] = CollarData.objects.filter(topic='collar/accel/X').last()
        context["Y"] = CollarData.objects.filter(topic='collar/accel/Y').last()
        context["Z"] = CollarData.objects.filter(topic='collar/accel/Z').last()
        context["bpm"] = CollarData.objects.filter(topic='collar/bpm').last()
        context["ketosis"] = CollarData.objects.filter(topic='collar/ketosis').last()
        context["mvmt"] = CollarData.objects.filter(topic='leg/mvmt/').last()

        context['temp_data'] = [float(x.message) for x in CollarData.objects.filter(topic='collar/temperature')]
        context['temp_ts'] = [x.timestamp.strftime("%H:%M:%S") for x in
                              CollarData.objects.filter(topic='collar/temperature')]

        context['bpm_data'] = [float(x.message) for x in CollarData.objects.filter(topic='collar/bpm')]
        context['bpm_ts'] = [x.timestamp.strftime("%H:%M:%S") for x in CollarData.objects.filter(topic='collar/bpm')]

        context['x_data'] = [float(x.message) for x in CollarData.objects.filter(topic='collar/X')]
        context['x_ts'] = [x.timestamp.strftime("%H:%M:%S") for x in CollarData.objects.filter(topic='collar/X')]

        context['bellow_data'] = [float(x.message) for x in CollarData.objects.filter(topic='collar/bellowing')]
        context['bellow_ts'] = [x.timestamp.strftime("%H:%M:%S") for x in
                                CollarData.objects.filter(topic='collar/bellowing')]

        # random.choice([1, 1, 1, 0, 1]) if float(x.message) == 1 else
        context['ketosis_data'] = [1 if float(x.message) == 1 else 0 for x in CollarData.objects.filter(topic='collar/ketosis')]
        context['ketosis_ts'] = [x.timestamp.strftime("%H:%M:%S") for x in
                                 CollarData.objects.filter(topic='collar/ketosis')]

        context['mvmt_data'] = [random.choice([1, 0, 0, 1]) if x.message == 'ACTIVITY' else 0 for x in
                                CollarData.objects.filter(topic='leg/mvmt/')]
        context['mvmt_ts'] = [x.timestamp.strftime("%H:%M:%S") for x in CollarData.objects.filter(topic='leg/mvmt/')]

        return self.render_to_response(context)


class ProfileView(TemplateView):
    template_name = 'dashboard/pages/user/user.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class DbToCSVView(TemplateView):
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
