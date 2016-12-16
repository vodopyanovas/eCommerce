# from django.contrib.auth.models import User
from shop_auth_app.models import MyUser
from django.http import JsonResponse


def validate_username(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': MyUser.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Exists!'
    return JsonResponse(data)
