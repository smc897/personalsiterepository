from django.shortcuts import render
from .models import Question, userinfo,about,project

# Create your views here.
from django.http import HttpResponse

#projects page
def projects(request,index):
    proj=project.objects.get(pk=index)
    length=len(project.objects.all())
    indexlowint=int(index)-1
    indexhighint=int(index)+1
    
    #clip high and low to max and min
    if int(index)>=length:
        indexhighint=length
        index=length
    if int(index)<=1:
        indexlowint=1
        index=1
    
    indexhigh=str(indexhighint)
    indexlow=str(indexlowint)
        
    template=loader.get_template('polls/projects.html')
    context = RequestContext(request, {
        'proj': proj,
        'index': index,
        'indexhigh':indexhigh,
        'indexlow':indexlow,
    })
    return HttpResponse(template.render(context))        

#about page
def aboutpage(request):
    about_list=about.objects.all()
    picturepath=about_list[0].path
    desc=about_list[0].description
    template = loader.get_template('polls/about.html')
    context = RequestContext(request, {
        'about_list': about_list,
        'picturepath':picturepath,
        'desc':desc,
    })
    return HttpResponse(template.render(context)) 

#contact page
def contact(request):
    latest_userinfo_list = userinfo.objects.all()
    name=latest_userinfo_list[0].name
    phone=latest_userinfo_list[0].phone
    email=latest_userinfo_list[0].email
    template = loader.get_template('polls/contact.html')
    context = RequestContext(request, {
        'latest_userinfo_list': latest_userinfo_list,
        'name':name,
        'phone':phone,
        'email':email,
    })
    return HttpResponse(template.render(context))    


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
    
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

#def vote(request, question_id):

#    return HttpResponse("You're voting on question %s." % question_id)
    
from django.template import RequestContext, loader

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
    })
    return HttpResponse(template.render(context))
    
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import Choice, Question
# ...
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
    
    