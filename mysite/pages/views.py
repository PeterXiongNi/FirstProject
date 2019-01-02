from django.shortcuts import render


def index(request):
    # return HttpResponse("<h1>The Peter Homepage</h1>")
    return render(request, 'pages/page.html')
