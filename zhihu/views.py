from django.shortcuts import render, get_object_or_404

from django.db.models import Count

from .models import Question, Answer

def index(request):
    all_answers = Answer.objects.all().order_by('-pub_time')

    context = {}
    context['all_answers'] = all_answers
    return render(request, 'zhihu/index.html', context)

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    # question归属话题, 取第一个话题
    question_topic = question.topics.all().first()
    # 话题相关question, 取前5个
    relate_questions = question_topic.question_set.all().order_by('-read_nums')[:5]

    context = {}
    context['question'] = question
    context['relate_questions'] = relate_questions
    return render(request, 'zhihu/question_detail.html', context)

def answer_detail(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    # 归属问题的其他推荐回答, 按点赞数和收藏数之和排序
    relate_answers = Answer.objects.all().\
        annotate(follow_nums=Count(userfollowanswer)).order_by('-follow_nums')[:5]

    context = {}
    context['answer'] = answer
    context['relate_answers'] = relate_answers
    return render(request, 'zhihu/answer_detail.html', context)