from django.http import HttpResponse

def key(request, key):
    if request.method == 'GET':
        return HttpResponse('{"key":"value"}', content_type='application/json')
