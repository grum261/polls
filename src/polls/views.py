from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

from .models import Poll, Question, Answer, Choice
from .permissions import IsOwner
from . import serializers


@csrf_exempt
@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


class PollViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = serializers.PollSerializer

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            self.permission_classes = (IsAuthenticated, IsOwner, IsAdminUser, )
        else:
            self.permission_classes = (AllowAny, )

        return super().get_permissions()


class ActivePollListView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Poll.objects.filter(end_date__gte=timezone.now()).filter(start_date__lte=timezone.now())
    serializer_class = serializers.PollSerializer


class QuestionViewSet(ModelViewSet):
    serializer_class = serializers.QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, IsAdminUser,)


class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = (IsAuthenticated, IsAdminUser, )


class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswerSerializer
    permission_classes = (IsAuthenticated, IsOwner, IsAdminUser, )
