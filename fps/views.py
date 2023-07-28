from django.http import HttpResponse, JsonResponse
from fps.models import Room


def index(request):
    return HttpResponse("FPS后端界面")


def get_room_list(request):
    rooms = []
    for room in Room.objects.all().order_by('port'):
        rooms.append({
                'name': room.name,
                'port': room.port
            })
    return JsonResponse({
        'error_message': "success",
        'rooms': rooms,
    })



def build_room(request):
    for port in [7777, 7778, 7779]:
        if not Room.objects.filter(port=port).exists():
            room = Room.objects.create(name="Room-%d" % port, port=port)
            return JsonResponse({
                    'error_message': "success",
                    'name': room.name,
                    'port': room.port,
            })
    return JsonResponse({
        'error_message': "no port available"
    })



def remove_room(request):
    port = int(request.GET.get('port'))
    Room.objects.filter(port=port).delete()
    return JsonResponse({
        'error_message': "success",
    })
