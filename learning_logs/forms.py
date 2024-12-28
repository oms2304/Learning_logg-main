from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm): # This form works with model Topic (hence the naming)
    class Meta: #tells Django which model to base the form off and which fields to include in the form
        model = Topic #specify which model the form will be based on
        fields = ['text'] # include the text field in the form
        labels = {'text':''}  #tells Django not to generate a label for the text


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})} #widgets is an HTML form element, single line box, list drop down, multiline text area
                                                             #here we are overwriting the default 40 columns and making it 80 so the user can write more

