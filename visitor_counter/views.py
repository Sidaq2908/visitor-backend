from django.http import JsonResponse
from .models import VisitorCounter

def increment_counter(request):
    counter, created = VisitorCounter.objects.get_or_create(pk=1)
    counter.count += 1
    counter.save()
    return JsonResponse({"count": counter.count})
