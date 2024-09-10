from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, TemplateView
from .forms import SignupForm


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"


class SignupView(CreateView):
    form_class = SignupForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("accounts:profile")

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password1"]
        user = authenticate(self.request, email=email, password=password)
        login(self.request, user)
        return response
