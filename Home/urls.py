from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^searchEvent$', views.searchEvent, name='searchEvent'),
    url(r'^news$', views.news, name='news'),
    url(r'^shortcourse$', views.shortcourse, name='shortcourse'),
    url(r'^survey$', views.survey, name='survey'),
    url(r'^workshops$', views.workshops, name='workshops'),
    url(r'^login$', views.login, name='login'),
    url(r'^registeration$', views.registeration, name='registeration'),
    url(r'^postshortcourse$', views.postshortcourse, name='postshortcourse'),
    url(r'^postsurvey$', views.postsurvey, name='postsurvey'),
    url(r'^forgetPassword$', views.forgetPassword, name='forgetPassword'),
    url(r'^postworkshop$', views.postworkshop, name='postworkshop'),
    url(r'^postEvent$', views.postEvent, name='postEvent'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^loginmsg$', views.loginmsg, name='loginmsg'),
]
