import random
import  logging
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from ball_app.models import Answer, Question

LOG = logging.getLogger(__name__)


def submit(request):
    all_answers = list(Answer.objects.all())
    current_answer = random.choice(all_answers)
    try:
        question = request.POST['question']
    except MultiValueDictKeyError:
        LOG.error("Request type is not post")
        return redirect('/')

    if not question:
        LOG.error("There was no question")

    model_q = Question(
        text=question,
        answer=current_answer
    )
    model_q.save()
    return redirect('/')


def get_question(request, question_id):
    question = Question.objects.get(pk=int(question_id))
    answer = question.answer
    return render(
        request,
        'index.html',
        {
            "question": question.text,
            "answer": answer.text
        }
    )


def index(request):
    return render(
        request,
        'index.html',
        {
            "history": Question.objects.all()
        }
    )