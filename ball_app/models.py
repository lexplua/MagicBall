from django.db import models


class Answer(models.Model):
    text = models.CharField(max_length=128)

    def __str__(self):
        return self.text


class Question(models.Model):
    text = models.TextField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)