from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    
    #ex \contact
    url(r'contact/$',views.contact, name='contact'),
    
    #ex /about
    url(r'about/$',views.aboutpage, name='about'),
    
    #ex /projects
    url(r'projects/(?P<index>[0-9]+)$',views.projects, name='projects'),   
    
]