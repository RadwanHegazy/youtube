from django.http import JsonResponse

def health_check_view(request) : 
    
    return JsonResponse({
        'message' : "successfully Running"
    })