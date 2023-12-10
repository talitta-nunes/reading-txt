from django import forms


class Form(forms.Form):
    files_data = forms.FileField()
