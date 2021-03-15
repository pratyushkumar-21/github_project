from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
import requests
from accounts.constants import BASE_URL

# Create your views here.
@login_required
def home(request):
    json_data = requests.get(BASE_URL + '/users/' +str(request.user))
    if (json_data.status_code == 200):
        data = json_data.json()
        render_data = {"data": data,}
        return render(request, 'home.html', render_data )
    else:
        return render(request, 'registration/login.html', {'msg' : "Something went wrong please try again!!!"})
