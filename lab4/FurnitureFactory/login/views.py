# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .forms import UserCreateForm
from factory.models import Client


class SignUpFormView(FormView):
    """
    form for registration
    """
    form_class = UserCreateForm
    success_url = '/auth/login/'

    template_name = 'signup.html'

    def form_valid(self, form) -> HttpResponse:
        form.save()
        print('creating')
        Client.objects.create(first_name=form.cleaned_data['first_name'],
                              last_name=form.cleaned_data['last_name'],
                              email=form.cleaned_data['email'],
                              birth_date=form.cleaned_data['birth_date'],
                              phone=form.cleaned_data['phone'],
                              city=form.cleaned_data['city'],
                              address=form.cleaned_data['address'],
                              image=form.cleaned_data['image']).save()
        print('created')
        return super(SignUpFormView, self).form_valid(form)

    def form_invalid(self, form) -> HttpResponse:
        return super(SignUpFormView, self).form_invalid(form)


class LoginFormView(FormView):
    """
    form for login + add API(gives you opportunity to share favourite quotes)
    """
    form_class = AuthenticationForm
    template_name = 'login.html'

    # print(quote)

    def get(self, request):
        return render(request, 'login.html', context={'form': self.form_class()})

    success_url = '/'

    def form_valid(self, form) -> HttpResponse:
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogOutView(View):
    """
    view for logging
    """

    def get(self, request):
        logout(request)

        return HttpResponseRedirect('/')
