from django import forms
from .models import Comment, Reply, Visitor

class AddVisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('name','email',)

class AddCommentForm(forms.Form):
    content = forms.CharField(max_length=650, required=True)
    def __init__(self, *args, **kwargs):
        super(AddCommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = forms.Textarea() 
        self.fields['content'].widget.attrs['rows'] = '3'
        self.fields['content'].widget.attrs['style'] = 'width:100%; padding:10px'
        self.fields['content'].widget.attrs['placeholder'] = 'Pleace leave a nice comment, and dont send a spam message :)'

class AddReplyForm(forms.Form):
    content = forms.CharField(max_length=650, required=True)
    def __init__(self, *args, **kwargs):
        super(AddReplyForm, self).__init__(*args, **kwargs)
        self.fields['content'].widget = forms.Textarea() 
        self.fields['content'].widget.attrs['rows'] = '3'
        self.fields['content'].widget.attrs['style'] = 'width:100%; padding:10px'
        self.fields['content'].widget.attrs['placeholder'] = 'Pleace leave a nice comment, and dont send a spam message :)'
