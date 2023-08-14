from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Profile
# Create your views here.


@csrf_exempt
def create_profile(request):
    if request.method == 'POST':
        data = request.POST
        name = data['name']
        email = data['email']
        
        if name and email:
            profile = Profile.objects.create(name=name,email=email)
            return JsonResponse({'Message': 'New profile was created!'})
        else:
            return JsonResponse({'Message': 'Some fields are missing, name and email are required!'})
    else:
        return JsonResponse({'Message': 'Invalid data'})
    
@csrf_exempt
def delete_profile(request,profile_id):
    profile = Profile.objects.get(id=profile_id)
    if request.method == "DELETE":
        profile.delete()
        return JsonResponse ({'Message': 'Profile was deleted'})
    else:
        return JsonResponse ({'Message': 'Invalid request'})
    
 
