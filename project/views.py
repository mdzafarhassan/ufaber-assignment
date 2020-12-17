from django.shortcuts import render, redirect
import requests
from django.conf import settings
# Create your views here.

api_host = settings.API_BASE_URL


def project_list(request):
    context = {}
    try:
        url = api_host
        response = requests.get(url)
        if response and response.status_code == 200:
            context['data'] = response.json
    except Exception as ex:
        print(ex)
    return render(request, 'project_list.html', context)


def project_create(request):
    context = {}
    if request.method == "POST" and request.FILES['avatar']:
        form_data = request.POST
        avatar = request.FILES['avatar']

        files = {avatar.name: avatar}
        print(files)
        data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'duration': form_data['duration']
        }

        url = api_host+"create_project/"
        response = requests.post(url, data, avatar={avatar.name: avatar})
        if response and response.status_code == 200:
            return redirect("/")
        else:
            print(38, response.json)
    return render(request, 'project_create.html', context)
