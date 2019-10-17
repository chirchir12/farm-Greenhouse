from django.shortcuts import render


def handler500(request, template_name='500.html'):
    response = render(request, "500.html")
    response.status_code = 500
    return response