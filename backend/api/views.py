import json
from django.http import JsonResponse


def api_home(request, *args, **kawargs):
    # request -> HttpRquest -> Django
    # request.body
    print(request.GET)
    body = request.body  # byte string of JSON data
    data = {}
    try:
        data = json.loads(body)  # string of JSON data -> Python Dict
    except:
        pass
    print(data)
    data["headers"] = dict(request.headers)
    data["content_type"] = request.content_type
    return JsonResponse(data)
