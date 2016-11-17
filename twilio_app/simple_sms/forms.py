from django import forms


class NameForm(forms.Form):
    number = forms.CharField(label='Number to send to! ', max_length=100)
    message_text = forms.CharField(label='Your message! ')
