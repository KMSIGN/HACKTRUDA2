from django import forms


class indexForm(forms.Form):
    # выпадающий список
    CHOICE_FIELDS = [
        (1, 'Кладовщик'),
        (2, 'Водитель погрузчик'),
        (3, 'Официант')
    ]

    url = forms.URLField(
        label='Введите ссылку с ваканией',
        help_text='Например с hh.ru',
        widget=forms.URLInput(attrs={'class': 'form-control'}),
        max_length=150,
        initial='value'
    )

    file = forms.FileField(
        label='Загрузите файл',
        widget=forms.FileInput(
            attrs={'class': 'custom-file-input', 'id': 'file'})
    )

    modelVac = forms.ChoiceField(
        label='Модель',
        choices=CHOICE_FIELDS,
        widget=forms.RadioSelect
    )


class personForm1(forms.Form, value):
    q1 = forms.CharField(
        label='Желаемая должность',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q2 = forms.CharField(
        label='У вас есть опыт работы кладовщиком?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q2d = forms.CharField(
        label='У вас есть опыт работы кладовщиком?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q3 = forms.CharField(
        label='Укажите Ваш стаж работы кладовщиком',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q4 = forms.CharField(
        label='Отрасль',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q5 = forms.CharField(
        label='Названия компаний',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q6 = forms.CharField(
        label='С какой системой хранения Вы имели опыт работы?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q7 = forms.CharField(
        label='Опыт работы с программами',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q8 = forms.CharField(
        label='Опыт с инструментарием',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q9 = forms.CharField(
        label='Типы работ',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q10 = forms.CharField(
        label='Сколько времени вы потратили на поиск работы кладовщика?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

    q11 = forms.CharField(
        label='Уровень ЗП (желаемый)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value',
    )

class personForm2(forms.Form):
    q1 = forms.CharField(
        label='Желаемая должность',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value'
    )

    q2 = forms.CharField(
        label='У вас есть опыт работы кладовщиком?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q2d = forms.CharField(
        label='У вас есть опыт работы кладовщиком?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q3 = forms.CharField(
        label='Укажите Ваш стаж работы кладовщиком',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q4 = forms.CharField(
        label='Отрасль',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q5 = forms.CharField(
        label='Названия компаний',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q6 = forms.CharField(
        label='С какой системой хранения Вы имели опыт работы?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q7 = forms.CharField(
        label='Опыт работы с программами',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q8 = forms.CharField(
        label='Опыт с инструментарием',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q9 = forms.CharField(
        label='Типы работ',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q10 = forms.CharField(
        label='Сколько времени вы потратили на поиск работы кладовщика?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q11 = forms.CharField(
        label='Уровень ЗП (желаемый)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

class personForm2(forms.Form):
    q1 = forms.CharField(
        label='Желаемая должность',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        initial='value'
    )

    q2 = forms.CharField(
        label='У вас есть опыт работы кладовщиком?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q2d = forms.CharField(
        label='У вас есть опыт работы кладовщиком?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q3 = forms.CharField(
        label='Укажите Ваш стаж работы кладовщиком',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q4 = forms.CharField(
        label='Отрасль',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q5 = forms.CharField(
        label='Названия компаний',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q6 = forms.CharField(
        label='С какой системой хранения Вы имели опыт работы?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q7 = forms.CharField(
        label='Опыт работы с программами',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q8 = forms.CharField(
        label='Опыт с инструментарием',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q9 = forms.CharField(
        label='Типы работ',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q10 = forms.CharField(
        label='Сколько времени вы потратили на поиск работы кладовщика?',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    q11 = forms.CharField(
        label='Уровень ЗП (желаемый)',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
