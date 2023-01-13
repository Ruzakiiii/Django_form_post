from django import forms

class UserForm(forms.Form):
    string_email = forms.EmailField(label='Ваш email ', help_text='email@gmail.com')

    string_phon_number = forms.CharField(label='Ваш номер +',help_text='+7 *** *** ** **', max_length=12,min_length=12)

    string_date = forms.DateField(label='В видите дату ',help_text='YYYY-MM-DD')

    string_text = forms.CharField(label='Ваш текст ')