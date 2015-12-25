from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate, login


# def index(request):
#     return HttpResponse("This page needs to be converted to a login Page\n")

# def index(request):
#     return HttpResponse("Hello World\n")

def detail(request, user_id):
    return HttpResponse("You're looking at %s - persons profile. ." % user_id)

def index(request):
    # context = {'user_id': user_id}
    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Succesful Login")
        else:
            HttpResponseRedirect((''))

    return render(request, 'user_login/log.html', context)

# def detail(request, user_id):
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)

 # if request.POST:
 #        username = request.POST['username']
 #        password = request.POST['password']

 #        user = authenticate(username=username, password=password)
 #        if user is not None:
 #            if user.is_active:
 #                login(request, user)
 #                return HttpResponse("Succesful Login\n")
 #    return render_to_response('login.html', context_instance=RequestContext(request))
