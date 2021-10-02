from django.shortcuts import render

# Create your views here.
def count_view(request):
    if 'count' in request.COOKIES:
        new_count=int(request.COOKIES["count"])+1
    else:
        new_count=1
    response=render(request,'PageCountApp/count.html',{'count':new_count})
    response.set_cookie('count',new_count)
    return response







