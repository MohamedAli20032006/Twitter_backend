from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet


# Create your views here.
def home_view(requests, *args, **kwargs):
    # return HttpResponse("<h1>I love you Nada</h1>")
    return render(requests, 'pages/home.html', context={}, status=200)

def tweet_detail_view(requests, tweet_id, *args, **kwargs):
    try:
        obj = Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    
    data = {
        'id': tweet_id,
        'content': obj.content,
        # 'image_path': obj.image.url,
    } 
    return JsonResponse(data)