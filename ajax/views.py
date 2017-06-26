from django.shortcuts import render, HttpResponse
from .models import *
from django.http import Http404, JsonResponse


def update_like(request, id):
    menu = C.objects.all()
    like = C.objects.get(id=id)
    auth = False
    if request.user.is_authenticated():
        user = UserProfile.objects.get(user_id=request.user)
        auth = True
        push_like = False
        you_post = False
        liking = like.liking.select_related()
        if like.author.user != user.user:
            for liker in liking:
                if liker == user.user:
                    push_like = True
        else:
            you_post = True
    return render(request, 'ajax/index.html', locals())



def add_ajax(request, id):
    if request.is_ajax():
        like = C.objects.get(id=id)
        user = UserProfile.objects.get(user_id=request.user.id)
        user.like -= 1
        user.save(update_fields=['like'])
        like.liking.add(user.user)
        like.author.like += 1
        like.author.save(update_fields=['like'])
        like.like += 1
        like.save(update_fields=['like'])
        response = {'count_like': str(like.like), 'available': user.like,'author': like.author.user.username, 'author-like': like.author.like}
        # return HttpResponse('OK')
        return JsonResponse(response)
    # else:
    #     raise Http404