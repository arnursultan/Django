from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from users.forms import UserRegistrationForm


class RegisterView(generic.FormView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('register-done')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get('password2')
        user.set_password(password)
        user.save()
        return super().form_valid(form)