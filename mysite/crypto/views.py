from django.shortcuts import render

def home(request):
    import requests
    import json

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api =  json.loads(api_request.content)
    return render(request, "home.html", {'api': api}) 


def body(request):
    import requests
    import json

    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api =  json.loads(api_request.content)
    for x in api.Data:
        body = x.body
        Body = body
    return render(request, "home.html", {'Body': Body} )
