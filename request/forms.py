from django.forms import ModelForm
from .models import Timeline, Request, Answer

class TimelineForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TimelineForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Timeline
        exclude = ('created','modified')
        labels = {
            'title': 'タイトル',
            'message': '内容',
            'progress': '進捗(％)',
            'shelter': '避難所'
        }

class RequestForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Request
        exclude = ('timeline','created','modified')

        labels = {
            'quantity': '必要数',
            'message': '必要なもの',
            'category': '種類',
            'timeline': '要求リスト'
        }

class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('created','modified')

