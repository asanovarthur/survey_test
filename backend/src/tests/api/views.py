from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView

from tests.models import Test, Question, TestResult, QuestionAnswer
from .serializers import TestSerializer, QuestionSerializer, TestResultSerializer, QuestionAnswerSerializer


class QuestionUpdateView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestUpdateView(UpdateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDestroyView(DestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestListView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionListView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestCreateView(CreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class QuestionCreateView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDestroyView(DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestResultListView(ListAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


class TestResultCreateView(CreateAPIView):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer


class QuestionAnswerCreateView(CreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
