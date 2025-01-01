from django.http import JsonResponse

def handler500(request):
    message = "Internal Server Error"
    response = JsonResponse(data={
        "error": message
    })
    response.status_code = 500
    return response