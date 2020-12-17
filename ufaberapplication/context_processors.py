from django.conf import settings


def context_processor(request):
    data = {
        'img_server': settings.IMG_SERVER
    }
    return {'custom_settings': data}
