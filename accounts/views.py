from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import WebSignUpForm


class SignUpView(CreateView):
    form_class = WebSignUpForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save()
        # EmailService.send_signup_email(self.object)
        return super().form_valid(form)
