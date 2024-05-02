from django.test import TestCase

from ball_app.models import Answer


class AnswerTestCase(TestCase):
    def setUp(self):
        Answer.objects.create(text="YES")

    def test_string_works(self):
        answer = Answer.objects.all().first()
        self.assertEquals(str(answer).lower(), "YES".lower())
