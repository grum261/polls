from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'polls', views.PollViewSet, basename='polls')
router.register(r'active/polls', views.ActivePollListView, basename='active_polls')
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'choices', views.ChoiceViewSet, basename='choices')
router.register(r'answers', views.AnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.login, name='login'),
]
