from .forms import LoginForm
from .models import CustomUser
from django.contrib.auth import login
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


# create custorm middleware
class MyAuthinticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.META["PATH_INFO"] == '/login/':
            if request.method == "POST":
                fm = LoginForm(data=request.POST)
                if fm.is_valid():
                    email = fm.cleaned_data['email']
                    user_password = fm.cleaned_data['password']
                    user = CustomUser.objects.filter(email=email).first()
                    if user is None:
                        messages.success(request, 'incorrect email')
                        return HttpResponseRedirect('/login')
                    if user_password != user.password:
                        messages.success(request, 'incorrect password')
                        return HttpResponseRedirect('/login')
                    login(request, user)
                    return HttpResponseRedirect('/profile/')

        response = self.get_response(request)
        return response


# for current time
c = datetime.now()
current_time = c.strftime('%H:%M:%S')


class GetIpAdress:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        current_url = request.path
        logger.info(f"[{current_time}] {ip} {current_url}")
        response = self.get_response(request)
        return response
