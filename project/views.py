from django.shortcuts import render, redirect
import requests
from django.conf import settings
import json
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

        url = api_host + "create_project/"
        response = requests.post(url, data, files={'avatar': avatar})
        if response and response.status_code == 201:
            return redirect("/")
    return render(request, 'project_create.html', context)


def project_delete(request, **kwargs):

    project_id = kwargs.get('project_id')
    print(project_id)
    url = api_host+f"{project_id}/delete/"
    print(url)
    response = requests.delete(url)
    print(response)
    if requests and response.status_code == 200:
        return redirect("/")
    else:
        print(requests.status_codes)


def project_update(request, **kwargs):
    project_id = kwargs.get('project_id')
    context = {'edit': True}
    if request.method == "POST":
        form_data = request.POST
        avatar = request.FILES['avatar']

        files = {avatar.name: avatar}
        print(files)
        data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'duration': form_data['duration']
        }

        url = api_host + f"{project_id}/update"
        response = requests.put(url, data, files={'avatar': avatar})
        return redirect("/")

    url = api_host + f"{project_id}/"
    print(url)
    response = requests.get(url)
    if response and response.status_code == 200:
        context['data'] = response.json
    return render(request, 'project_create.html', context)


def project_view(request, **kwargs):
    project_id = kwargs.get('project_id')
    context = {}
    url1 = api_host + f"{project_id}/"

    response1 = requests.get(url1)
    if response1 and response1.status_code == 200:
        context['project'] = response1.json
        url2 = api_host + f"{project_id}/task/"
        response2 = requests.get(url2)
        if response2 and response2.status_code == 200:
            context["task_list"] = response2.json
    return render(request, 'task_view.html', context)
