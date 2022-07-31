from django.http import JsonResponse
from seat.models import Seat

# Create your views here.
def get_list(request):
    # find all and jsonify
    seats = Seat.objects.all()
    return JsonResponse(list(seats.values()), safe=False)