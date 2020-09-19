from django import forms

class indexForm(forms.Form):
    url = forms.URLField(label='Введите ссылку с ваканией') #, upload_to='uploads/'
    file = forms.FileField(label='Загрузить файл')
    modelVac = forms.ChoiceField(choices=(('goo', '1111'), ('dooo', '2222')))