from django.http import JsonResponse


def my_view(request):
    return JsonResponse({'hello': 'world'})
