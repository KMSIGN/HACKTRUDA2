from django import forms

class indexForm(forms.Form):
    url = forms.URLField(label='Введите ссылку с ваканией') #, upload_to='uploads/'
    file = forms.FileField(label='Загрузить файл')
    modelVac = forms.ChoiceField(choices=(('1', '1111'), ('2', '2222')))