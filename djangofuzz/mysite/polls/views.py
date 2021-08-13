from django.core.mail import send_mail, EmailMessage
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Question, Choice, FilePathFieldForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def send(request):
    # subject = '主题'  # 主题
    # message = 'sssssss'  # 内容
    # sender = 'my@qq.com'  # 发送邮箱，已经在settings.py设置，直接导入
    # receiver = ['target@qq.com']  # 目标邮箱
    # html_message = '<h1>%s</h1>' % 'testtesttest'  # 发送html格式
    # send_mail(subject, message, sender, receiver, html_message=html_message)

    email = EmailMessage(
        'Hello',
        'Body goes here',
        'from@example.com',
        ['to1@example.com', 'to2@example.com'],
        ['bcc@example.com'],
        reply_to=['another@example.com'],
        headers={'Message-ID': 'foo'},
    )
    email.send()


# 使用form组件实现注册方式
def manage_FilePathForm(request):
    form_obj = FilePathFieldForm()         # 实例化一个对象
    if request.method == "POST":
        # 实例化form对象的时候，把post提交过来的数据直接传进去
        form_obj = FilePathFieldForm(request.POST)
        # 调用form_obj校验数据的方法
        if form_obj.is_valid():
            form_obj.save()
    return render(request, 'polls/manage_authors.html', {'form_obj': form_obj})