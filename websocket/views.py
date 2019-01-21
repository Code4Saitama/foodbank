from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'websocket/index.html', {})

def room(request):
    return render(request, 'websocket/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })
