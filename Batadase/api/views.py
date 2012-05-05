from django.http import HttpResponse
from django.utils.simplejson import loads, dumps

from api.models import Key, Value

def key(request, key):
    if request.method == 'GET':
        try:
            key_obj = Key.objects.get(key=key)
            dict = {key:key_obj.value_set.all()}
        except Key.DoesNotExist:
            dict = {key:[]}
        json = dumps(dict)
        return HttpResponse(json, content_type='application/json')
    if request.method == 'POST':
        key_obj = Key.objects.get(key=key)
        Value.objects.create(key=key_obj)
