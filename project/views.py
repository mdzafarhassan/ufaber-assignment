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
    except:
        pass
    return render(request, 'project_list.html', context)


def project_create(request):
    context = {}
    if request.method == "POST" and request.FILES['avatar']:
        form_data = request.POST
        avatar = request.FILES['avatar']

        files = {avatar.name: avatar}
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

    url = api_host+f"{project_id}/delete/"
    response = requests.delete(url)
    if requests and response.status_code == 200:
        return redirect("/")


def project_update(request, **kwargs):
    project_id = kwargs.get('project_id')
    context = {'edit': True}
    if request.method == "POST":
        form_data = request.POST
        avatar = request.FILES['avatar']

        data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'duration': form_data['duration']
        }

        url = api_host + f"{project_id}/update"
        response = requests.put(url, data, files={'avatar': avatar})
        return redirect("/")

    url = api_host + f"{project_id}/"
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
    return render(request, 'project_view.html', context)


def task_create(request, **kwargs):
    project_id = kwargs.get('project_id')
    context = {}
    if request.method == "POST":
        form_data = request.POST

        data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'start_date': form_data['start_date'],
            'end_date': form_data['end_date']
        }

        url = api_host + f"{project_id}/create_task/"
        response = requests.post(url, data)
        if response and response.status_code == 201:
            return redirect(f"/project/{project_id}/")

    url = api_host + f"{project_id}/"
    print(url)
    response = requests.get(url)
    if response and response.status_code == 200:
        context['project'] = response.json
    return render(request, 'task_create.html', context)


def task_delete(request, **kwargs):
    project_id = kwargs.get('project_id')
    task_id = kwargs.get('task_id')
    url = api_host + f"{project_id}/{task_id}/delete/"
    print(url)
    response = requests.delete(url)
    if requests and response.status_code == 200:
        return redirect(f"/project/{project_id}/")


def task_update(request, **kwargs):
    project_id = kwargs.get('project_id')
    task_id = kwargs.get('task_id')
    context = {'edit': True}

    if request.method == "POST":
        form_data = request.POST

        data = {
            'name': form_data['name'],
            'description': form_data['description'],
            'start_date': form_data['start_date'],
            'end_date': form_data['end_date']
        }

        url = api_host + f"{project_id}/{task_id}/update"
        response = requests.put(url, data)
        return redirect(f"/project/{project_id}/")

    url = api_host + f"{project_id}/{task_id}"
    response = requests.get(url)
    if response and response.status_code == 200:
        context['data'] = response.json
    return render(request, 'task_create.html', context)
