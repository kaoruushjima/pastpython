from django.http.response import HttpResponse

def home(request):
    return HttpResponse ('HELLO WORLD')

def room(request, room_id):
    return HttpResponse("this is a room detail " + room_id)